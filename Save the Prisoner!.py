t=int(input())
for i in range(0,t):
    x=input()
    n,m,s=x.split()
    n=int(n)
    m=int(m)
    s=int(s)
    ctr=s
    g=n%m
    for j in range(0,g):
        if ctr>n:
            ctr=ctr%n
        ctr+=1
    print(ctr)
