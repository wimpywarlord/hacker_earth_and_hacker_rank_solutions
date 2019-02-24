n=int(input())
z=list(map(int,input().split()))
xx=max(z)
ans=0
for i in range(0,len(z)):
    ans+=z[i]
ans=ans-(xx//2)
print(ans)
