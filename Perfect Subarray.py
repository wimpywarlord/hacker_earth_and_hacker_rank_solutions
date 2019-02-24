n=int(input())
l=list(map(int,input().split()))
sub=[]
ctr=0
def ps(x):
    for i in range(1,1000):
        if x==i**2:
            return 1
    return 0
for i in range(0,len(l)):
    for j in range(0,len(l)-i):
        sub.append([])
        for k in range(i,len(l)-j):
            #print(l[k],end=' ')
            sub[ctr].append(l[k])
        ctr+=1
        #print()
#print(sub)
summ=[]
for i in range(0,len(sub)):
    ss=0
    for j in range(0,len(sub[i])):
        ss+=sub[i][j]
    summ.append(ss)
#print(summ)
ans=0
for i in range(0,len(summ)):
    if ps(summ[i])==1:
        ans+=1
print(ans)
