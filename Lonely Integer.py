n=int(input())
arr=list(map(int,input().split()))
from collections import defaultdict
d=defaultdict(int)
for i in range(0,len(arr)):
    d[arr[i]]+=1
#print(arr)
for i in range(0,len(arr)):
    if d[arr[i]]==1:
        print(arr[i])
        break
    
