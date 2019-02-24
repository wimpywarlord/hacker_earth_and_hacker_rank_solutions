z=input()
n,m=z.split()
n=int(n)
m=int(m)
s=input()
ss=s.split()
for i in range(0,len(ss)):
    ss[i]=int(ss[i])
#print(ss)
l=[]
for i in range(0,n):
    if i in ss:
        l.append(1)
    else:
        l.append(0)
#print(l)
ans=[]
for i in range(0,len(l)):
    temp=[]
    for j in range(0,len(l)):
        if l[j]==1:
            temp.append(abs(j-i))
            ctr=0
    ans.append(min(temp))
print(max(ans))
            
