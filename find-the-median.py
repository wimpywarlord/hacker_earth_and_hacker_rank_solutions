n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr[len(arr)//2])
