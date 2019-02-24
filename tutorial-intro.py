ele=int(input())
l=int(input())
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    if arr[i]==ele:
        print(i)
        break
