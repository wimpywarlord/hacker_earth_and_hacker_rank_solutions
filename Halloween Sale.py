z=input()
p,d,m,s=z.split()
p=int(p)
d=int(d)
m=int(m)
s=int(s)
l=[]
for i in range(1,100000):
    if l[i-1]-d>m:
        l.append(a[i-1]-d)
    else:
        l.append(m)
#print(l)
ctr=0
ans=0
while ans<=s:
    ans+=l[ctr]
    if ans>=s:
        break
    #print(ans)
    ctr+=1
if m==1:
    print(ctr+1)
else:
    print(ctr)
