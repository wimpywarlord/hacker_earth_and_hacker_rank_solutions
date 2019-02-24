n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
x=max(l2)
y=min(l1)
use1=0
use2=0
for i in range(0,len(l1)):
    if l1[i]<x:
        use1+=x-l1[i]
for i in range(0,len(l2)):
    if l2[i]>y:
        use2+=l2[i]-y
print(min(use1,use2))
