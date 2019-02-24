n=int(input())
count=0
arr=list(map(int,input().split()))
if sum(arr)%2==1:
    print("NO")
else:
    for i in range(0,len(arr)):
        if arr[i]%2!=0:
            arr[i]+=1
            arr[i+1]+=1
            count+=2
    print(count)
