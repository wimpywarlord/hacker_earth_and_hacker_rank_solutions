n=int(input())
x=input()
y=input()
dom=x.split()
brian=y.split()
for i in range(0,len(dom)):
    dom[i]=int(dom[i])
    brian[i]=int(brian[i])
print(brian)
print(dom)
d=[]
b=[]
diffd=0
diffb=0
for j in range(0,len(dom)):
    if j!=len(dom)-1:
        diffd=abs(dom[j+1]-dom[j])
        diffb=abs(brian[j+1]-brian[j])
        d.append(diffd)
        b.append(diffb)
if max(d)>max(b):
    print("Dom")
    print(max(d))
else:
    print("Brian")
    print(max(b))
