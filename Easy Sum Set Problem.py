'''n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
b=[]
for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        b.append(arr2[j]-arr1[i])
#print(*b)
for i in range(0,len(arr1)):
    for j in range(0,len(b)):
        if arr1[i]+b[j] not in arr2:
            b[j]=-10000
#print(b)
ctr=0
for i in range(0,len(b)):
    if b[i-ctr]==-10000:
        del b[i-ctr]
        ctr+=1
b.sort()
print(*set(b))

'''
n=input()
a=list(map(int,input().rstrip().split()))
m=input()
c=list(map(int,input().rstrip().split()))
b=[]
for i in c:
    for j in a:
        if(i>j):
            b.append(i-j)
b=list(set(b))
z=[]
for i in a:
    for j in b:
        if(c.count(i+j)==0):
            z.append(j)
z=list(set(z))       
for i in z:
    b.remove(i)
b.sort()
print(*b)


