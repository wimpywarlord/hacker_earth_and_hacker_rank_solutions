'''n=int(input())
l=list(input().split())
for i in range(0,len(l)):
    l[i]=l[i].lstrip('0')
#print(l)
from collections import OrderedDict
d=OrderedDict()
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        d[l[i][j]]=0
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        d[l[i][j]]+=1
#print(d)
val=list(d.values())
#print(val)
key=list(d.keys())
#print(key)
use=max(val)
#print(use)
for i in range(0,len(val)):
    if val[i]==use:
        usekey=key[i]
        break
print(usekey)
ans=0
for i in range(0,len(l)):
    flag=0
    for j in range(0,len(l[i])):
        if l[i][j]==usekey:
            flag=1
    if flag==1:
        ans+=1
print(ans)'''
            
'''ans=0
for i in range(len(l)-1,-1,-1):
    flag=0
    for j in range(0,len([i])):
        if l[i][j]==usekey:
            ans=i
            flag=1
            break
    if flag==1:
        break
print(ans+1)'''

# Write your code here
n=int(input())
array=list(map(str,input().split(' ')))
maximum=0
character=['0','1','2','3','4','5','6','7','8','9']
for value in character:
    count=0
    for val in array:
        if value in val:
            count+=1
            if maximum<count:
                maximum=count
print(maximum)
