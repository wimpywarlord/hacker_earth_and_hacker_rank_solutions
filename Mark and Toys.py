n,spend=map(int,input().split())
#print(n,spend)
arr=list(map(int,input().split()))
arr.sort()
used=0
ctr=0
while ctr<n and spend>used:
    if used+arr[ctr]>spend:
        break
    else:
        used+=arr[ctr]
        ctr+=1
print(ctr)
