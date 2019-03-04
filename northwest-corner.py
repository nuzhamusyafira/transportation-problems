cost=[
	  [14,9,16,18],
	  [11,8,7,6],
	  [16,12,10,22]
     ]
supply=[150,210,320]
demand=[130,70,180,240]

def pojokKiriAtas(s,d):
	table=[]
	for x in range(s):
		temp=[]
		for y in range(d):
			temp.append(0)
		table.append(temp)
	toAllocate(table,0,0)
	return table

def toAllocate(table2,x,y):
	global sTot,dTot
	if sTot==0 and dTot==0:
		return table2
	if supply[x]<demand[y]:
		table2[x][y]=supply[x]
		demand[y]-=supply[x]
		supply[x]=0
		sTot=sum(supply)
		dTot=sum(demand)
		toAllocate(table2,x+1,y)
	elif supply[x]>demand[y]:
		table2[x][y]=demand[y]
		supply[x]-=demand[y]
		demand[y]=0
		sTot=sum(supply)
		dTot=sum(demand)
		toAllocate(table2,x,y+1)
	elif supply[x]==demand[y]:
		table2[x][y]=supply[x]
		supply[x]=0
		demand[y]=0
		sTot=sum(supply)
		dTot=sum(demand)
		toAllocate(table2,x+1,y+1)

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

resultTable=pojokKiriAtas(s,d)
print("Cost Tableau:")
for row in cost:
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
		print("x%d"%(cost[x][y]),end='')
		if x<s-1 or y<d-1:
			flag=1
		ongkos+=resultTable[x][y]*cost[x][y]
print(" =",ongkos)