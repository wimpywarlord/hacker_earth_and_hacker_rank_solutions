n=int(input())
z=input()
l=z.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
'''v=[]
for i in range(0,len(l)):
    v.append([])
    v[i].append(l[i])
    for j in range(0,len(l)):
        if abs(l[i]-l[j])<=1 and j!=i:
            v[i].append(l[j])
#print(v)
g=[]
for i in range (0,len(v)):
    flag=0
    for j in range(0,len(v[i])):
        for k in range(0,len(v[i])):
            if abs(v[i][j]-v[i][k])>1:
                flag=1
    if flag==0:
        g.append(len(v[i]))
print(max(g))'''
v=[]
g=[]
for i in range(0,len(l)):
    v.append([])
    g.append([])
    v[i].append(l[i])
    g[i].append(l[i])
    for j  in range(0,len(l)):
        if l[i] - l[j]==1 or l[i]-l[j]==0 and j!=i:
            v[i].append(l[j])
    for k in range(0,len(l)):
        if l[i]-l[k]==-1 or l[i]-l[k]==0 and k!=i:
            g[i].append(l[k])
ans1=[]
ans2=[]
for i in range(0,len(v)):
    ans1.append(len(v[i]))
for i in range(0,len(g)):
    ans2.append(len(g[i]))
a=max(ans1)
b=max(ans2)
if a>b:
    print(a)
else:
    print(b)
            
            
        
        
