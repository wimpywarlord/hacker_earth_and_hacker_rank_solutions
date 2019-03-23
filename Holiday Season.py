n=int(input())
a=input()
ans=0
for i in range(0,n-3):
    for j in range(i,n-1):
        if a[i]==a[j] and i!=j:
            for k in range(i,j+1):
                for l in range(j+1,n):
                    if a[k]==a[l] and k!=l and i!=k and i!=l and j!=l and j!=k:
                        #print(a[i],i,a[k],k,a[j],j,a[l],l)
                        ans+=1
print(ans)
        
