n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.sort()
l2.sort()
#print(l1)
#print(l2)
ans=0
for i in range(0,len(l1)):
    ans+=abs(l1[i]-l2[i])
print(ans%(7+10**9))
