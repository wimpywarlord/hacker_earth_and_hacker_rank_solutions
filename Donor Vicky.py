t=int(input())
for i in range(0,t):
    y=input()
    n,x=y.split()
    n=int(n)
    x=int(x)
    donate=0
    ctr=1
    while donate<=x:
        donate+=ctr
        ctr+=1
        if ctr<=n:
            pass
        else:
            ctr=ctr%n
    print(ctr)
            
