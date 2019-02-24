n,k,q=map(int,input().split())
#print(n)
k=k%n
#print(k)
#print(q)
s=list(map(int,input().split()))
#print(s)
use=[]
for i in range(0,q):
    z=int(input())
    use.append(z)
#print(use)
ans=[]
ctr=0
for i in range(0,len(s)):
    ans.append(0)
for i in range(0,k):
    ans[i]=s[n-k+ctr]
    ctr+=1
ptr=0
for i in range(k,len(s)):
    ans[i]=s[ptr]
    ptr+=1
#print(ans)
for i in range(0,len(use)):
    print(ans[use[i]])
