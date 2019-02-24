n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
from collections import defaultdict
d1= defaultdict(int)
d2= defaultdict(int)
for i in range(0,n):
    d1[arr1[i]]+=1
for i in range(0,m):
    d2[arr2[i]]+=1

d1key=list(d1.keys())
#print(d1key)
d1val=list(d1.values())
d2key=list(d2.keys())
#print(d2key)
d2val=list(d2.values())
lll=[]
for i in range(0,len(d2key)):
    if d2key[i] not in d1key:
        lll.append(d2key[i])
    elif d2[d2key[i]] > d1[d2key[i]]:
        lll.append(d2key[i])
lll=set(lll)
#print(lll)
lll=list(lll)
lll.sort()
for i in range(0,len(lll)):
    print(lll[i],end=' ')
    
    
