'''n,k=map(int,input().split())
arr=list(map(int,input().split()))
ctr=0
arr.sort()
for i in range(n):
    for j in range(i,n):
        if arr[j]-arr[i]==k:
            ctr+=1
        
print(ctr)'''
n,k=map(int,input().split())
arr=list(map(int,input().split()))
ctr=0
arr.sort()
i=0
j=1
while j<n:
    diff = arr[j] -arr[i]
    if diff==k:
        ctr+=1
        j+=1
    elif diff>k :
        i+=1
    elif diff<k:
        j+=1
print(ctr)
