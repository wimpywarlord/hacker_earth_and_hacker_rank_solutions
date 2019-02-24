n=int(input())
l=list(map(int,input().split()))
#print(l)
sub=[]
subctr=0
x=len(l)
for i in range(0,x):
    for j in range(0,x-i):
        sub.append([])
        for k in range(i,x-j):
            sub[subctr].append(l[k])
        subctr+=1
#print(sub)
scorel=[]
sizel=[]
x=len(sub)
for i in range(0,x):
    for j in range(0,x-i):
        size=0
        score=0
        for k in range(i,x-j):
            for m in range(0,len(sub[k])):
                score+=sub[k][m]
            size+=1
        scorel.append(score//size)
        sizel.append(size)
#print(scorel)
z=max(scorel)
for i in range(0,len(scorel)):
    if scorel[i]==z:
        print(scorel[i],sizel[i])
        break
#print(sizel)
            
