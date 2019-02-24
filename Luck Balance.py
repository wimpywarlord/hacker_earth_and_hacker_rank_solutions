n,k=map(int,input().split())
#print(k)
l=[]
for i in range(0,n):
    l.append([])
    use1,use2=map(int,input().split())
    l[i].append(use1)
    l[i].append(use2)
#print(l)
l = sorted(l, key=lambda x: x[0],reverse=True)
#print(l)
ans=0
for i in range(0,n):
    if l[i][1]==1 and k>0:
        k-=1
        ans+=l[i][0]
    elif l[i][1]==1 and k<=0:
        ans-=l[i][0]
        k-=1
    elif l[i][1]==0:
        ans+=l[i][0]
    #print(ans,k)
print(ans)
