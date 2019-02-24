'''z=input()
n,d=z.split()
n=int(n)
d=int(d)
q=input()
l=q.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
ctr=0
l.sort()
for i in range(0,len(l)):
    for j in range(i,len(l)):
        for k in range(j,len(l)):
            if l[j]-l[i]==d and l[k]-l[j]==d:
                ctr+=1
print(ctr)'''
n,d=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n-2):
    if l[i]+d in l and l[i]+2*d in l:
        c+=1
print (c)
    
