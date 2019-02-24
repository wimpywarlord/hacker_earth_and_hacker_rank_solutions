x=input()
n,k=x.split()
n=int(n)
k=int(k)
y=input()
h=y.split()
for i in range(0,len(h)):
    h[i]=int(h[i])
print(h)
g=max(h)-k
if g>0:
    print(max(h)-k)
else:
    print(0)
