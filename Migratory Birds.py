n=int(input())
s=input()
l=s.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
d={}
for i in range(0,len(l)):
    d[l[i]]=0
#print(d)
for i in range(0,len(l)):
    d[l[i]]+=1
f=list(d.values())
h=list(d.keys())
f.sort()
#print(f)
g=f[len(f)-1]
#print(g)
for i in range(0,len(h)):
    if d[h[i]]==g:
        print(h[i])
        break

    
