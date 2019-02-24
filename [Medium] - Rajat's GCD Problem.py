import math
t=int(input())
for i in range(0,t):
    z=list(map(int,input().split()))
    xxx=z[0]**z[2]+z[1]**z[2]
    #print(xxx)
    yyy=abs(z[0]-z[1])
    #print(yyy)
    print(math.gcd(xxx,yyy)%(10**9+7))
