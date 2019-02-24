t=int(input())
from collections import defaultdict 
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    def defaultvalue():
        return 0
    #print(arr)
    d=defaultdict(defaultvalue)
    for j in range(0,n):
        d[arr[j]]+=1
    keys=list(d.keys())
    vals=list(d.values())
    #print(d)
    for i in range(0,len(vals)):
        if vals[i]!=3:
            print(keys[i])
            break
        
