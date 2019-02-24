n,k=map(int,input().split())
arr=list(map(int,input().split()))
k=k%n
k=k
ans=[]
for i in range(0,n):
    ans.append(0)
for i in range(0,k):
    ans[n-k+i]=arr[i]
#print(ans)
for i in range(0,n-k):
    ans[i]=arr[k+i]
#print(ans)
for i in range(0,n):
    print(ans[i],end=' ')
