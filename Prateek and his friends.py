t=int(input())
for i in range(0,t):
    y=input()
    n,x=y.split()
    n=int(n)
    x=int(x)
    f=[]
    for i in range(0,n):
        g=int(input())
        f.append(g)
    flag=0
    for i in range(0,n):
        counter=n
        for j in range(i,n):
            summ=0
            for k in range(i,counter):
    
               summ+=f[k]
            if summ==x:
                flag=1
            else:
                pass
            counter-=1
            
    if flag==1:
        print("YES")
    else:
        print("NO")
