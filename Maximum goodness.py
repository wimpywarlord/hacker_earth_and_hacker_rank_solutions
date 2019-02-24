n=int(input())
s=list(map(int,input().split()))
#print(s)
suba=[]
ctr=0
for i in range(0,len(s)):
    for j in range(0,len(s)-i):
        suba.append([])
        for k in range(i,len(s)-j):
            #print(s[k],end=' ')
            suba[ctr].append(s[k])
        ctr+=1
        #print()
#print(suba)
l=[]
use=[]
for i in range(0,len(suba)):
    l.append(len(suba[i]))
    ptr=0
    for j in range(0,len(suba[i])):
        if suba[i][j]==1:
            ptr+=1

        if suba[i][j]==0:
            ptr-=1

    use.append(ptr)
#print(l)
#print(use)
ans=[]
z=max(use)
for i in range(0,len(use)):
    if use[i]==z:
        ans.append(l[i])
print(max(ans))
