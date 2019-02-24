z=input()
n,m=z.split()
n=int(n)
m=int(m)
p=input()
l1=p.split()
for  i in range(0,len(l1)):
    l1[i]=int(l1[i])
q=input()
l2=q.split()
for i in range(0,len(l2)):
    l2[i]=int(l2[i])
print(l1)
print(l2)
a=max(l1)
b=max(l2)
ctr=0
for i in range(a,b+1):
    flag1=0
    flag2=0
    for j in range(0,len(l1)):
        if i%l1[j]!=0:
            flag1=1
    for j in range(0,len(l2)):
        if l2[j]%i!=0:
            flag2=1
    if flag1==0 and flag2==0:
        ctr+=1
print(ctr)
    
    
