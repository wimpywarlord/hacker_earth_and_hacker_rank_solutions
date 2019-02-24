x=input()
n,k=x.split()
n=int(n)
k=int(k)
ll=[]
for i in range(0,k):
    y=input()
    l=y.split()
    for i in range(0,len(l)):
        l[i]=int(l[i])
    ll.append(l)
for  i in range(0,len(ll)):
    del ll[i][0]
for i in range(0,len(ll)):
    if not ll[i]:
        ll[i].append(0)
print(ll)
q=int(input())
for i in range(0,q):
    v=input()
    a,b=v.split()
    a=int(a)
    b=int(b)
    ini=0
    fin=0
    hh=0
    ee=0
    for j in range(0,len(ll)):
        for f in range(0,len(ll[j])):
            if ll[j][f]==a:
                ini=j
            if ll[j][f]==b:
                fin=j
    if fin>=ini:
        hh=fin-ini
        ee=ini+len(ll)-fin
        print(min(ee,hh))
    if ini>fin:
        hh=ini-fin
        ee=fin+len(ll)-ini
        print(min(ee,hh))
                
                
    
