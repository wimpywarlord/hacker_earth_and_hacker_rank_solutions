t,n=map(int,input().split())
arr=[]
for i in range(0,t):
    z=list(input())
    arr.append(z)
#print(arr)
import math
use=math.factorial(t)//(math.factorial(t-2)*math.factorial(2))
#print(use)
p=[]
pctr=0
for i in range(0,use):
    for j in range(i+1,t):
        p.append([])
        p[pctr].append(i)
        p[pctr].append(j)
        pctr+=1
#print(p)
final=[]
for i in range(0,use):
    temp=''
    for j in range(0,n):
        if arr[p[i][0]][j]=='0' and arr[p[i][1]][j]=='0':
            temp+='0'
        else:
            temp+='1'
    ans=0
    #print(temp)
    for j in range(0,n):
        if temp[j]=='1':
            ans+=1
    final.append(ans)
zzz=max(final)
print(zzz)
ctr=0
for i in range(0,use):
    if final[i]==zzz:
        ctr+=1
print(ctr)
