cost=[
	  [10,0,20,11],
	  [12,7,9,20],
	  [0,14,16,18]
     ]
supply=[15,25,5]
demand=[5,15,15,10]

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

def multi(row, col, Cost, Allocate):
	print("a")
	U = [] 
	V = []
	Penalty = []
	for i in range(row):
		temp=[]
		for j in range(col):
			temp.append(1)
		Penalty.append(temp)
	maxx = -1
	maxy = -1
	while(1):
		for r in Penalty:
			print(r)
		U.append(0)
		for i in range(1,row):
			U.append(-1)

		for i in range(col):
			print(col)
			V.append(-1)

		for i in range(row):
			for j in range(col):
				if Allocate[i][j]>0:
					if U[i]!=-1:
						V[j]=Cost[i][j]-U[i]
					else:
						U[i]=Cost[i][j]-V[j]
					Penalty[i][j]=0
	            
		for i in range(row):
			for j in range(col):
				if Allocate[i][j]==0:
					Penalty[i][j]=Cost[i][j]-U[i]-V[j]
		        
				if maxx == -1 or Penalty[i][j] > Penalty[maxx][maxy]:
					maxx = i
					maxy = j
	    
		if maxx == -1 or Penalty[maxx][maxy] > 0:
			print("Optimal Solution has already been reached.")
			return Penalty

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

resultTable1=pojokKiriAtas(s,d)
resultTable=multi(s,d,cost,resultTable1)
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