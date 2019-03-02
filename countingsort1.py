n=int(input())
arr=list(map(int,input().split()))
from collections import OrderedDict
d1=OrderedDict()
for i in range(0,100):
    d1[i]=0
#print(d1)
for i in range(0,n):
    d1[arr[i]]+=1
for i in range(0,100):
    print(d1[i],end=' ')
    
