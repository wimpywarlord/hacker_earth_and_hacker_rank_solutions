n=int(input())
l=[]
ctr=0
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            l.append([])
            l[ctr].append(i)
            l[ctr].append(j)
            l[ctr].append(k)
            ctr+=1
#print(l)
final=[]
for i in range(0,len(l)):
    summ=0
    for j in range(0,len(l[i])):
        summ+=l[i][j]
    if summ==n:
        final.append(l[i])
dup=[]
for i in range(0,len(final)):
    for j in range(0,len(final[i])):
        if final[i][0]>final[i][1] and final[i][1]>final[i][2]:
            dup.append(final[i])
#print(dup)
ans=[]
for  i in range(0,len(dup)):
    if dup[i] not in ans:
        ans.append(dup[i])
print(len(ans))

    
    
