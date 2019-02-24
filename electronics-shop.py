x=input()
b,n,m=x.split()
b=int(b)
n=int(n)
m=int(m)
y=input()
lk=y.split()
for  i in range(0,len(lk)):
    lk[i]=int(lk[i])
z=input()
lm=z.split()
for j in range(0,len(lm)):
    lm[j]=int(lm[j])
v=[]
for i in range(0,len(lm)):
    for j in range(0,len(lk)):
        v.append(lm[i]+lk[j])
print(v)
if min(v)>b:
    print(-1)
else:
    zz=[]
    for i in range(0,len(v)):
        if v[i]<=b:
            zz.append(v[i])
    print(max(zz))
    
