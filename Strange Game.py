t=int(input())
for  i in range(0,t):
    n,k=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    z=max(arr2)
    ans=0
    for i in range(0,len(arr1)):
        if arr1[i]<=z:
            ans+=((z+1-arr1[i])*k)
    print(ans)
