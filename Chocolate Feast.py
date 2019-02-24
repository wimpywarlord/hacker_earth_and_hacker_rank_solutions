t=int(input())
for i in range(0,t):
    z=input()
    n,c,m=z.split()
    n=int(n) #MONEY TO SPEND
    c=int(c) #COST OF CHOCOLATE
    m=int(m) #NUMBER OF WRAPPERS REQUIRED TO GET A CHOCOLATE
    cw=n//c
    ans=n//c
    while cw>=m and m<=ans:
        cw-=m
        cw+=1
        ans+=1
    print(ans) 
#41894 36 640
