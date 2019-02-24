t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    #print(arr)
    maxx=0
    ctr=0
    for j in range(0,len(arr)):
        if arr[j]%2==0:
            ctr+=1
        if arr[j]%2!=0 or j==len(arr)-1:
            if maxx<ctr:
                maxx=ctr
            ctr=0
    if maxx==0:
        print(-1)
    else:
        print(maxx)
