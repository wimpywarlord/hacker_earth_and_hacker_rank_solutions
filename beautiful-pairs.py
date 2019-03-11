from collections import defaultdict
n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
d1=defaultdict(int)
d2=defaultdict(int)
for j in range(0,n):
    d1[arr1[j]]+=1
    d2[arr2[j]]+=1
print(d1)
print(d2)
d2key=list(d2.keys())
d1key=list(d1.keys())
print(d1key)
print(d2key)
for j in range(0,len(d2key)):
    if d2key[j] not in d1:
        for k in range(0,len(d1key)):
            if d1[d1key[k]]==2:
                d1key[k]=d2key[j]
                break
print(d1)
print(d2)
            
        
