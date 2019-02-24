t=int(input())
for i in range(0,t):
    n,p,q,r=map(int,input().split())
    #print(n)
    #print(p)
    #print(q)
    #print(r)
    lp=[]
    lq=[]
    lr=[]
    for j in range(0,n+1,p):
        if j!=0:
            lp.append(j)
    for j in range(0,n+1,q):
        if j!=0:
            lq.append(j)
    for j in range(0,n+1,r):
        if j!=0:
            lr.append(j)
    #print(lp)
    #print(lq)
    #print(lr)
    ans=0
    for j in range(0,len(lp)):
        if lp[j] not in lq and lp[j] not in lr:
            ans+=1
    for j in range(0,len(lq)):
        if lq[j] not in lp and lq[j] not in lr:
            ans+=1
    for j in range(0,len(lr)):
        if lr[j] not in lp and lr[j] not in lq:
            ans+=1
    print(ans)
