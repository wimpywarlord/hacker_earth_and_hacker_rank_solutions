'''
n=int(input())
arr=list(input())
from collections import OrderedDict
d=OrderedDict()
for i in range(0,len(arr)):
    #print(arr[i])
    if arr[i] not in d:
        d[arr[i]]=1
    else:
        d[arr[i]]+=1
ans=''
dkey=list(d.keys())
for i in range(0,len(d)):
    if d[dkey[i]]%2==1:
        ans+=dkey[i]
#print(d)
print(len(ans))
print(ans)
'''
n=int(input())
arr=list(input())
stack=[]
for i in range(0,len(arr)):
    stack.append(0)
top=0
for i in range(0,len(arr)):
    if stack[top]!=arr[i]:
        top+=1
        stack[top]=arr[i]
    elif stack[top]==arr[i]:
        stack[top]=0
        top-=1
#print(stack)
ans=''
for i in range(0,len(stack)):
    if stack[i]!=0:
        ans+=stack[i]
print(len(ans))
print(ans)
    
