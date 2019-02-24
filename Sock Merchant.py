n=int(input())
x=input()
l=x.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
d={}
for i in range(0,len(l)):
    d[l[i]]=0
for i in range(0,len(l)):
    d[l[i]]+=1
a=list(d.values())
#print(a)
ctr=0
for i in range(0,len(a)):
    ctr+=a[i]//2
print(ctr)
