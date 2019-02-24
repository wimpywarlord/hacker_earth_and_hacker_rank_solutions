import math
t=int(input())
for i in range(0,t):
    l,r=map(int,input().split())
    a=(l)**(1/2)
    b=(r)**(1/2)
    a=math.ceil(a)
    b=math.floor(b)
    print(b-a+1)
    '''ans=0
    for j in range(l,r+1):
        if math.floor((j)**(1/2))==math.ceil((j)**(1/2)):
            ans+=1
    print(ans)'''
