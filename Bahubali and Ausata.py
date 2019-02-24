e=input()
n,q=e.split()
n=int(n)
q=int(q)
x=input()
a=x.split()
for i in range(0,len(a)):
    a[i]=int(a[i])
for j in range(0,q):
    y=input()
    l,r=y.split()
    l=int(l)
    r=int(r)
    summ=0
    for k in range(l-1,r):
        summ=summ+a[k]
    avg=summ//(r - l + 1 )
    print(avg)
        
