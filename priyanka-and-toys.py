n=int(input())
arr=list(map(int,input().split()))
arr.sort()
#print(arr)
ctr=0
ptr=0
ans=1
while ctr<n:
    if arr[ctr]<=arr[ptr]+4:
        #print(arr[ptr],arr[ctr])
        ctr+=1
    else:
        ptr=ctr
        ans+=1
print(ans)
