t=int(input())
for i in range(0,t):
    n=int(input())
    nn=[]
    nn.append(n)
    print(nn)
    l=[]
    while n>0:
        r=n%10
        l.append(r)
        n=n//10
    l=l[::-1]
    ans=0
    for i in range(0,len(l)):
        if l[i]!=0 and nn[0]%l[i]==0:
            ans+=1
    print(ans)
