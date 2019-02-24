n=int(input())
arr=list(map(int,input().split()))
maxx=-1
for i in range(0,len(arr)):
    sum1=0
    sum2=0
    for j in range(0,i):
        sum1+=arr[j]
    for j in range(i,len(arr)):
        sum2+=arr[j]
    if sum1*sum2>maxx:
        maxx=sum1*sum2
print(maxx)
