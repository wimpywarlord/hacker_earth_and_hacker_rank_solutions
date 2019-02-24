n=int(input())
f=[]
count=0
for i in range(0,n):
    for j in range(0,n):
        if i * j == n :
            f.append([])
            f[count].append(i) 
            f[count].append(j)
            count+=1
print(f)
sumlist=[]
summ=0
for k in range(0,len(f)):
    summ=0
    for l in range(0,2):
        summ=summ+f[k][l]
    sumlist.append(summ)
print(sumlist)
print(min(sumlist))
