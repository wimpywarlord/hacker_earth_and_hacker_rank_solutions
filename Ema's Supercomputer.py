n,m=map(int,input().split())
l=[]
for i in range(0,n):
    s=list(input())
    l.append(s)
#print(l)
l.insert(0,[])
for j in range(0,len(l[i])):
    l[0].insert(j,0)
l.append([])
for j in range(0,len(l[i])):
    l[len(l)-1].insert(j,0)
for i in range(0,len(l)):
    l[i].insert(0,0)
for i in range(0,len(l)):
    l[i].append(0)   
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        pass
        #print(l[i][j],end=' ')
    #print()
ans=[]
for i in range(0,len(l)):
    ans.append([])
    for j in range(0,len(l[i])):
        area=0
        ctr=1
        if l[i][j]=='G':
            while True:
                if l[i][j+ctr]=='G' and l[i][j-ctr]=='G' and l[i+ctr][j]=='G' and l[i-ctr][j]=='G':
                    ctr+=1
                else:
                    break

        ans[i].append(ctr)
#print(ans)
for i in range(0,len(ans)):
    for j in range(0,len(ans[i])):
        pass
        #print(ans[i][j],end='   ')
    #print()
ans.insert(0,[])
for j in range(0,len(ans[i])):
    ans[0].insert(j,0)
ans.append([])
for j in range(0,len(ans[i])):
    ans[len(ans)-1].insert(j,0)
for i in range(0,len(ans)):
    ans[i].insert(0,0)
for i in range(0,len(ans)):
    ans[i].append(0)
#print()

for i in range(0,len(ans)):
    for j in range(0,len(ans[i])):
        pass
        #print(ans[i][j],end='   ')
    #print()
    
use=[]

for h in range(0,2):
    z=max(max(ans))
    #print(z)
    for i in range(0,len(ans)):
        for j in range(0,len(ans[i])):
            if z==ans[i][j]:
                use.append(ans[i][j])
                ptr=0
                while True:
                    ptr+=1
                    ans[i][j+ptr]=-1
                    ans[i][j-ptr]=-1
                    ans[i+ptr][j]=-1
                    ans[i-ptr][j]=-1
                    if ptr==ans[i][j]:
                        break
                ans[i][j]=-1
                break
#print()

for i in range(0,len(ans)):
    for j in range(0,len(ans[i])):
        pass
        #print(ans[i][j],end='   ')
    #print()
  
#print(use)
output=1
for i in range(0,len(use)):
    output=output*(1+(use[i]-1)*4)
print(output)
