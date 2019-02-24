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
for i in range(n):
    for j in range(n):        
        if j==y and i==x-1 :
            a[i][j]=p - 1
        if j==y and i==x+1 :
            a[i][j]=p - 1
        if i==x and j==y+1 :
            a[i][j]=p - 1
        if i==x and j==y-1 :
            a[i][j]=p - 1
        if i==x-1 and j==y-1:
            a[i][j]=p - 1
        if i==x+1 and j==y+1:
            a[i][j]=p - 1
        if i==x+1 and j==y-1:
            a[i][j]=p - 1
        if i==x-1 and j==y+1:
            a[i][j]=p - 1
    
            
print()
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
