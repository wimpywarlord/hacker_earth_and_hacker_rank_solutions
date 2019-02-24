n=int(input())
z=input()
l=z.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
v=[]
ptr=0
for i in range(0,len(l)):
    ctr=0
    for j in range(i,len(l)):
        v.append([])
        for k in range(i,len(l)-ctr):
            print(l[k],end='')
            v[ptr].append(l[k])
        ptr+=1
        print()
        ctr+=1
print(v)
ans=0
for i in range(0,len(v)):
    flag=0
    for j in range(0,len(v[i])):
        for k in  range(0,len(v[i])):
            if abs(v[i][j]-v[i][k])>1:
                flag=1
    
    if flag==0:
        ans+=1
        print(v[i])
print(ans)
        
            
