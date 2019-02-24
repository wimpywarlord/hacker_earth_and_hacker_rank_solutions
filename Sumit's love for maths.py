t=int(input())
for i in range(0,t):
    z=list(map(int,input().split()))
    ans=0
    for j in range(1,z[0]+1):
        if j%z[1]==0 or j%z[2]==0 or j%z[3]==0:
            ans+=1
    print(ans)
