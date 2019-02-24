n=int(input())
r=input()
x,y,p=r.split()
x=int(x)
y=int(y)
p=int(p)
a=[]
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(0)
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
a[x][y]=p

            

                 
print()
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
