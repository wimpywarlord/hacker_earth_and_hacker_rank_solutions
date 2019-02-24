n=int(input())
z=input()
a=z.split()
for i in range(0,len(a)):
    a[i]=int(a[i])
x=len(a)
a.append(0)
a.append(0)
#print(a)
i=0
ctr=0
while i<x:
    print(i)
    if i>=x-1:
        break
    elif a[i+1]==0 and a[i+2]==0:
        ctr+=1
        i+=2
    elif a[i+1]==1 and a[i+2]==0:
        ctr+=1
        i+=2
    elif a[i+1]==0 and a[i+2]==1:
        ctr+=1
        i+=1

print(ctr)
