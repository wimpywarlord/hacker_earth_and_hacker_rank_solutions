n=int(input())
l=list(map(int,input().split()))
#print(l)
sub=[]
subctr=0
for i in range(0,len(l)):
    for j in range(0,len(l)-i):
        sub.append([])
        for k in range(i,len(l)-j):
            sub[subctr].append(l[k])
        subctr+=1
#print(sub)
subsub=[]
subsubctr=0
for i in range(0,len(sub)):
    for j in range(0,len(sub)-i):
        subsub.append([])
        for k in range(i,len(sub)-j):
            subsub[subsubctr].append(sub[k])
        subsubctr+=1
#print(subsub)
#print()
'''for i in range(0,len(subsub)):
    for j in range(0,len(subsub[i])):
        pass
        print(subsub[i][j],end='   ')
    print()'''
score=[]
for i in range(0,len(subsub)):
    use=0
    for j in range(0,len(subsub[i])):
        for k in range(0,len(subsub[i][j])):
            use+=subsub[i][j][k]
    score.append(use//len(subsub[i]))
print(max(score))
