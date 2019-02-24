z=input()
n,k=z.split()
n=int(n)
k=int(k)
y=input()
arr=y.split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
#print(arr)
ctr=1
ans=0
for i in range(0,len(arr)):
    ptr=0
    for j in range(1,arr[i]+1):
        ptr+=1
        if ptr>k:
            ptr=1
            ctr+=1
        if ctr==j:
            #print(j)
            ans+=1
    ctr+=1
print(ans)
            
