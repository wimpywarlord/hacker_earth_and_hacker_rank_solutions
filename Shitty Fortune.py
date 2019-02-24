t=int(input())
for i in range(0,t):
    s=input()
    a,n=s.split()
    n=int(n)
    d=[]
    u=[]
    r=len(a)//n
    for i in range(0,n):
        d.append([])
        u.append([])
        for j in range(0,r):
            d[i].append(a[j])
            u[i].append(a[j])
    print(d)
    print(u)
    ctr=0
    for i in range(0,len(d)):
        for j in range(0,len(d[i])):
            ctr+=1
    if ctr!=len(a):
        print("NO")
    else:
        flag=0
        for i in range(0,len(d)):
            d[i].reverse()
            print(d[i])
            print(u[i])
            if u[i]==d[i]:
                pass
            else:
                flag=1
        if flag==1:
            print("NO")
        else:
            print("YES")
