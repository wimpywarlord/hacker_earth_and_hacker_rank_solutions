t=int(input())
for i in range(0,t):
    y=input()
    x,b=y.split()
    x=int(x)
    b=int(b)
    ans=((b//x)-1)*(b//x)//2
    print(ans)
