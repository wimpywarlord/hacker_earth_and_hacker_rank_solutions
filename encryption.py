s=input()
import math
for i in range(0,len(s)):
    row=math.floor((len(s))**(1/2))
    col=math.ceil((len(s))**(1/2))
#print(row)
#print(col)
if row*col>len(s):
    sol=[]
    ctr=0
    for i in range(0,row):
        sol.append([])
        for j in range(0,col):
            if ctr<len(s):
                sol[i].append(s[ctr])
                ctr+=1
            else:
                sol[i].append(' ')
    #print(sol)
    for j in range(0,len(sol[i])):
        for i in range(0,len(sol)):
            if sol[i][j]!=' ':
                print(sol[i][j],end='')
        print(end=' ')
else :
    row+=1
    sol=[]
    ctr=0
    for i in range(0,row):
        sol.append([])
        for j in range(0,col):
            if ctr<len(s):
                sol[i].append(s[ctr])
                ctr+=1
            else:
                sol[i].append(' ')
    #print(sol)
    for j in range(0,len(sol[i])):
        for i in range(0,len(sol)):
            if sol[i][j]!=' ':
                print(sol[i][j],end='')
        print(end=' ')
