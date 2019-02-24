n=int(input())
l=list(map(int,input().split()))
#print(l)
sub=[]
subctr=0
x=len(l)
for i in range(0,x):
    for j in range(0,len(l)-i):
        sub.append([])
        for k in range(i,len(l)-j):
            sub[subctr].append(l[k])
        subctr+=1
#print(sub)
subsub=[]
subsubctr=0
sizel=[]
for i in range(0,len(sub)):
    for j in range(0,len(sub)-i):
        subsub.append([])
        size=0
        for k in range(i,len(sub)-j):
            for m in range(0,len(sub[k])):
                subsub[subsubctr].append(sub[k][m])
            size+=1
        sizel.append(size)
        subsubctr+=1
'''for i in range(0,len(subsub)):
    for j in range(0,len(subsub[i])):
        print(subsub[i][j],end=' ')
    print()'''
#print(sizel)
ans=[]
for i in range(0,len(subsub)):
    score=0
    for j in range(0,len(subsub[i])):
        score+=subsub[i][j]
    ans.append(score//sizel[i])
print(max(ans))
        
#print(subsub)
