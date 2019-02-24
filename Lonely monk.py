n=int(input())
x=input()
a=x.split()
for i in range(0,n):
    a[i]=int(a[i])

print(a)

d=[]
for i in range(0,n):
    counter=n
    for j in range(i,n):
        
        summ=0
        for k in range(i,counter):
           print(a[k],end=' ')
           summ=summ+a[k]
        counter-=1
        print()
        print(summ)
        d.append(summ)        
        print()
    print()
print(d)
gg=0
for i in range(0,len(d)):
    if d[i]%2==0:
        gg+=1
print(gg)
            
