arr=list(map(int,input().split()))
sum1=0
sum2=0
ctr=0
for i in range(0,len(arr)):
    if ctr%2==0:
        sum1+=arr[i]
    else:
        sum2+=arr[i]
    ctr+=1
print(sum1)
print(sum2)
