t=int(input())
for i in range(0,t):
    z=input()
    n,k,q=z.split()
    n=int(n)
    k=int(k)
    q=int(q)
    ll=input()
    l=ll.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    jump=n//k
    p=[]
    for j in range(0,len(l)):
        p.append([])
        for k in range(j,j+jump):
            p[j].append(l[k])
    print(p)
            
