h=int(input())
n=int(input())  
tower=[]
for i in range(0,h):
    tower.append([])
    for j in range(0,3):
        tower[i].append(1)
ctr=0
for i in range(0,n):
    s=input()
    ctr+=1
    t,p=s.split()
    t=int(t)-1
    print("LEVEL :",t,end=' ')
    print("BLOCK :",p)
    if p=='R': 
        cc=2
    if p=='L':
        cc=0
    if p=='M':
        cc=1
    print(cc)
    tower[t][cc]=0
    for j in range(0,len(tower)):
        for k in range(0,len(tower[j])):
            print(tower[j][k],end=' ')
        print()
    flag=0
    for j in range(0,len(tower)):
        for k in range(0,len(tower[j])):
            if k==0 or k==1:
                if tower[j][k]==0 and tower[j][k+1]==0:
                    if tower[j-1]!=[0,0,0]:
                        flag=1
                        break
        if flag==1:
            break
    if flag==1:
        break
if flag==1:  
    print(ctr)
else:
    print(-1)
        
        
    
    
    
 

