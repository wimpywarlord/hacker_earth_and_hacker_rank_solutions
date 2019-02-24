z=input()
n,t=z.split()
n=int(n)
t=int(t)
w=input()
l=w.split()
for j in range(0,len(l)):
    l[j]=int(l[j])
for i in range(0,t):
    p=input()
    r,s=p.split()
    r=int(r)
    s=int(s)
    v=[]
    for j in range(r,s+1):
        v.append(l[j])
    print(min(v))
    
    
