t=int(input())
for i in range(0,t):
    n=int(input())
    l=[]
    t=[]
    for j in range(0,n+1):
        l.append(j)
    print(l)
    summ=0
    summlist=[]
    diff=0
    t=[]
    s=0
    for k in range(0,len(l)):
        s=s+l[k]
        summlist.append(summ)
    for k in range(0,len(l)):
        if k!=len(l)-1:
            summ+=l[k]
            print(summ)
            diff=l[n]-l[k]
            print(diff)
            if n==1:
                t.append(1)
            else:
                t.append(summ+diff+abs(summ-diff))
    print(t)
    print(min(t))
