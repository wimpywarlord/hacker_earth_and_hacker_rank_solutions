n=int(input())
arr=list(map(int,input().split()))
k=int(input())
from collections import defaultdict
d=defaultdict(int)
for i in range(n):
    d[arr[i]]+=1
ans=[]
dkey=list(d.keys())
for i in range(len(dkey)):
    if d[dkey[i]]==k:
        ans.append(dkey[i])
print(min(ans))
