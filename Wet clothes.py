n,m,g=map(int,input().split())
#print(n,m,g)
tlist=list(map(int,input().split()))
alist=list(map(int,input().split()))
#print(tlist)
#print(tlist)
#print(alist)
uset=0
ans=0
for i in range(0,len(tlist)-1):
    x=(tlist[i+1]-tlist[i])
    if uset<x:
        uset=x
#print(uset)
ans=0
for i in range(0,len(alist)):
    if uset>=alist[i]:
        #print(uset,alist[i])
        ans+=1
#print(alist)
print(ans)
