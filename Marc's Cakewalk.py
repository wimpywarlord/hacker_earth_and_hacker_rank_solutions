n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
ctr=0
ans=0
for i in range(0,n):
    ans+=((2**i)*arr[i])
print(ans)
    
    
