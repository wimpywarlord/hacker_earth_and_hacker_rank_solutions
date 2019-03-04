n=int(input())
arr=list(map(int,input().split()))
arr.sort()
for i in range(0,n):
    print(arr[i],end=' ')

