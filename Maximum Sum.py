n=int(input())
arr=list(map(int,input().split()))
ans=0
ctr=0
ptr=0
for i in range(0,n):
    if arr[i]<0 :
        ptr+=1
if ptr==n:
    print(max(arr),'1')
else:
    for i in range(0,n):
        if arr[i]>=0:
            ans+=arr[i]
            ctr+=1
    print(ans,ctr)
        
