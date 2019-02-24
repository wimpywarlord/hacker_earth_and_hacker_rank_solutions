q=input()
s,x,n=q.split()
s=int(s)
x=int(x)
n=int(n)
t1=[]
y1=[]
for i in range(0,n):
    qq=input()
    t,y=qq.split()
    t1.append(int(t))
    y1.append(int(y))
print(t1)
print(y1)
ctr=0
while s>=0:
    ctr+=1
    for j in range(n):
        if t1[j]==ctr:
            s=s-y1[j]
    s=s-x
print(ctr)
