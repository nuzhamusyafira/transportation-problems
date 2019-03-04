cost=[
	  [14,9,16,18],
	  [11,8,7,6],
	  [16,12,10,22]
     ]
supply=[150,210,320]
demand=[130,70,180,240]

def vogel(s,d):
	table=[]
	for x in range(s):
		temp=[]
		for y in range(d):
			temp.append(0)
		table.append(temp)
	toAllocate(table,s,d)
	return table

def toAllocate(table2,s,d):
	global sTot,dTot,iters
	if sTot==0 and dTot==0:
		return table2
	sortedRow=sortCost(s,d,0)	
	sortedCol=sortCost(d,s,1)	
	pRow=penaltyVal(sortedRow)	
	pCol=penaltyVal(sortedCol)	
	sortedAll=sortAll(pRow,pCol)	
	indexRow=indexCell(s,d,0)		
	indexCol=indexCell(d,s,1)		
	direc=sortedAll[0][3]
	if direc==0:
		idx=sortedAll[0][2]
		x=indexRow[idx][0][1]
		y=indexRow[idx][0][2]
	elif direc==1:
		idx=sortedAll[0][2]
		x=indexCol[idx][0][1]
		y=indexCol[idx][0][2]
	if supply[x]<demand[y]:
		table2[x][y]=supply[x]
		demand[y]-=supply[x]
		supply[x]=0
		sTot=sum(supply)
		dTot=sum(demand)
		for a in range(d):
			cost[x][a]=1000000
		toAllocate(table2,s,d)
	elif supply[x]>demand[y]:
		table2[x][y]=demand[y]
		supply[x]-=demand[y]
		demand[y]=0
		sTot=sum(supply)
		dTot=sum(demand)
		for z in range(s):
			cost[z][y]=1000000
		toAllocate(table2,s,d)
	elif supply[x]==demand[y]:
		table2[x][y]=supply[x]
		supply[x]=0
		demand[y]=0
		sTot=sum(supply)
		dTot=sum(demand)
		for a in range(d):
			cost[x][a]=1000000
		for z in range(s):
			cost[z][y]=1000000
		toAllocate(table2,s,d)

def sortCost(d,s,flag):
	box=[]
	for x in range(d):
		temp=[]
		for y in range(s):
			if flag==1:
				temp.append(cost[y][x])
			else:
				temp.append(cost[x][y])
		temp2=sorted(temp)
		box.append(temp2)
	return box

def penaltyVal(lists):
	penBox=[]
	x=0
	for row in lists:
		if(len(row)==1):
			penalty=row[0]
		else:
			penalty=row[1]-row[0]
		temp=[]
		temp.insert(0,penalty)
		temp.insert(1,row[0])
		temp.insert(2,x)
		penBox.append(temp)
		x+=1
	return penBox

def indexCell(d,s,flag):
	box=[]
	for x in range(d):
		temp2=[]
		for y in range(s):
			temp=[]
			if flag==1:
				temp.insert(0,cost[y][x])
				temp.insert(1,y)
				temp.insert(2,x)
			else:
				temp.insert(0,cost[x][y])
				temp.insert(1,x)
				temp.insert(2,y)
			temp2.append(temp)
		temp2=sorted(temp2)
		box.append(temp2)
	return box

def sortAll(row,col):
	box=[]
	for x in row:
		x+=[0]
		box.append(x)
	for x in col:
		x+=[1]
		box.append(x)
	box.sort(key=lambda z: (-z[0], z[1]))
	return box

sTot=sum(supply)
dTot=sum(demand)
s=len(supply)
d=len(demand)
if sTot<dTot:
	s+=1
	supply.append(dTot - sTot)
	sTot=sum(supply)
	temp=[]
	for x in range(len(demand)):
		temp.append(0)
	cost.append(temp)

elif sTot>dTot:
	d+=1
	demand.append(sTot - dTot)
	dTot=sum(demand)
	for x in range(len(supply)):
		cost[x].append(0)

import copy
cost2=copy.deepcopy(cost)
resultTable=vogel(s,d)
print("Cost Tableau:")
for row in cost2:
	print(row)
print("\nAllocation Tableau:")
for row in resultTable:
	print(row)
print("\nOngkos Minimum:")
ongkos=0
flag=0
for x in range(s):
	for y in range(d):
		if resultTable[x][y]==0:
			continue
		if flag==1:
			print(" + ", end='')
		print("%d"%(resultTable[x][y]),end='')
		print("x%d"%(cost2[x][y]),end='')
		if x<s-1 or y<d-1:
			flag=1
		ongkos+=resultTable[x][y]*cost2[x][y]
print(" =",ongkos)