n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=1000000
for i in range(0,n):
    if i != n-1:
        if abs(arr[i]-arr[i+1])<m:
            m=abs(arr[i]-arr[i+1])
print(m)
