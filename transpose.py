n=int(input())
m=int(input())
a=[]
for i in range(0,n):
    a.append([])
    for j in range(0,m):
        x=int(input())
        a[i].append(x)
temp=0
b=[]
for k in range(0,n):
    print()
    b.append([])
    for l in range(0,m):
         b[k].append(a[l][k]) 
         #print(a[l][k],end=' ')
print(b)

for k in range(0,n):
    for l in range(0,m):
        if l == 2:
            pass
        else:
            temp=a[k][l]
            a[k][l]=a[l][k]
            a[l][k]=temp
    break
for k in range(n - 1,-1,-1):
    for l in range(m - 1 ,-1,-1):
        temp=a[k][l]
        a[k][l]=a[l][k]
        a[l][k]=temp
    break
print(a)
