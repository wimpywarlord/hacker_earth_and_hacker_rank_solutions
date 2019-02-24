t=int(input())
for i in range(0,t):
    n=int(input())
    x=input()
    y=input()
    a=x.split()
    for i in range(0,n):
        a[i]=int(a[i])
    print(a)
    b=y.split()
    for i in range(0,n):
        b[i]=int(b[i])
    print(b)
    suma=0
    sumb=0
    for i in range (0,n):
        suma=suma+a[i]
        sumb=sumb+b[i]
    if suma==sumb:
        print("YES")
    else:
        print("NO")
