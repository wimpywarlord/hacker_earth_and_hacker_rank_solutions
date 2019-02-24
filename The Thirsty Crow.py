t=int(input())
for i in range(0,t):
    z=input()
    a,b,h,w=z.split()
    a=int(a)
    b=int(b)
    h=int(h)
    w=int(w)
    n=int(input())
    g=input()
    u=g.split()
    for j in range(0,len(u)):
        u[j]=int(u[j])
    limit=h
    level=w
    ctr=0
    u.sort(reverse=True)
    while level<=limit:
        if ctr<len(u):
            level+=u[ctr]
            ctr+=1
    print(ctr)
