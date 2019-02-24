n=int(input())
arr=list(map(int,input().split()))
z=sum(arr)
print(z)
if n==1 and arr[0]!=0:
    print("NO")
elif z%2==0:
    print("YES")
else:
    print("NO")
