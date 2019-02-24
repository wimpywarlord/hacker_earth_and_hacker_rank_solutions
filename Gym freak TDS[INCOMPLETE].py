import math
x=input()
n,w=x.split()
n=int(n)
w=int(w)
y=input()
ps=y.split()
z=input()
ws=z.split()
for i in range(0,len(ws)):
    ws[i]=int(ws[i])
    ps[i]=int(ps[i])
ws.sort()
taken=0
pro=0
j=0
while taken<=w:
    if taken+ws[j]<=w:
        print("@")
        taken+=ws[j]
        pro+=ps[j]
        print(pro)
    elif taken+ws[j]>w:
        print("$")
        taken+=ws[j]
        print((ps[j]*(ws[j]-(taken-w)))/ws[j])
        pro+=math.floor((ps[j]*(ws[j]-(taken-w)))/ws[j])
        
    j+=1
print(pro)
