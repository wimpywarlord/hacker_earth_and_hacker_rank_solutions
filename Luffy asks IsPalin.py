def isodd(ee):
    if ee%2==0:
        return False
    else:
        return True
t=int(input())
for i in range(0,t):
    x=input()
    n,q=x.split()
    n=int(n)
    q=int(q)
    aa=input()
    a=[]
    for g in range(0,len(aa)):
        a.append(aa[g])
    print(a)
    for j in range(0,q):
        y=input()
        l,r=y.split()
        l=int(l)
        r=int(r)
        d=dict()
        for k in range(l-1,r):
            d[a[k]]=0
        for k in range(l-1,r):
            d[a[k]]+=1
        print(d)
        ctr=0
        for k in range(l-1,r):
            z=isodd(d[a[k]])
            if z==True:
                ctr+=1
        if ctr>=2 :
            print("NO")
        else:
            print("YES")
