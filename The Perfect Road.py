t=int(input())
for i in range(0,t):
    z=input()
    s,x,n=z.split()
    s=int(s)
    x=int(x)
    n=int(n)
    y=input()
    l=y.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    zz=max(l)
    ctr=0
    for j in range(0,len(l)):
        if l[j]==zz:
            ctr+=1
    if ctr==1:
        for j in range(0,len(l)):
            if l[j]==zz:
                print(j+1)
                break
    else:
        print("Many Roads")
        
