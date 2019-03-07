n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
ctr=0
ans=0
for i in range(0,n):
    flag=0
    while flag==0:
        z=arr1[0]
        
        #print(arr1,arr2[i])
        #print(arr2[i],arr1[0])
        if arr2[i]==arr1[0]:
            del arr1[0]
            ans+=1
            flag=1
        else:
            ans+=1
            for j in range(1,len(arr1)):
                arr1[j-1]=arr1[j]
            arr1[-1]=z

        
print(ans)
    
