y=int(input())
arr=list(map(int,input().split()))
n=int(input())
for j in range(0,y):
    if arr[j]==n:
        print(j)
        break
