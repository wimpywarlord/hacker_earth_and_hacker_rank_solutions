n=int(input())
arr=list(map(int,input().split()))
use=sum(arr)
for i in range(0,n):
    flag=0
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            flag=1
    if flag==0:
        print(arr[i],end=' ')

