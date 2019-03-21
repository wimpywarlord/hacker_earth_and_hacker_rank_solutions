'''
n=int(input())
arr=list(map(int,input().split()))
use2=set(arr)
use=[]
for i in range(0,n):
    for j in range(0,n):
        temp=''
        for k in range(i,n-j):
            #print(arr[k],end='')
            temp+=str(arr[k])
        if temp!=' ' and temp!='':
            use.append(temp)
        #print()

print(use2)
ans=0
for i in range(0,len(use)):
    if len(set(use[i]))==use2:
        ans+=1
print(ans)
'''
n=int(input())
arr=list(map(int,input().split()))
use=set(arr)
ans=0

for i in range(0,n):
    s=set()
    for j in range(i,n):
        if s!=use:
            s.add(arr[j])
            if s==use:
                ans+=1
        else:
            ans+=1
        #print(s)
print(ans)
