t=int(input())
ans=0
for i in range(t):
    z=int(input())
    z=z-1
    ctr=0
    while z>0:
        z=z//2
        ctr+=1
    ans+=ctr
print(ans)
