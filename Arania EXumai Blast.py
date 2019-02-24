b=input()
a=b.split()
c=[]
counter=0
for i in a:
    c.append([])
    for j in i:
        c[counter].append(j)
    counter+=1
print(c)
count=0
for k in range(0,len(c)):
    for l in range(0,len(c[k])-1):
        if a[k][l]==a[k][l+1]:
            count+=1
print(count)
        
