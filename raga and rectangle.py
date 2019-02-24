x=input()
r,c=x.split()
r=int(r)
c=int(c)
f=[]
for i in range(0,r):
    f.append([])
    for j in range(0,c):
        y=input()
        f[i].append(y)
count=0
for j in range(0,c):
    if f[r//2][j]=='W' or f[r//2][j]=='w':
        count+=1
print(count//2)

