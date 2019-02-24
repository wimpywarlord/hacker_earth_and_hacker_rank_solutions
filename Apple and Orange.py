x=input()
s,t=x.split()
s=int(s)
t=int(t)
#print(s)
#print(t)
y=input()
a,b=y.split()
a=int(a)
b=int(b)
#print(a)
#print(b)
z=input()
m,n=z.split()
m=int(m)
#print(m)
n=int(n)
#print(n)
apple=input()
applel=apple.split()
for i in range(len(applel)):
    applel[i]=int(applel[i])
orange=input()
orangel=orange.split()
for i in range(0,len(orangel)):
    orangel[i]=int(orangel[i])
#print(applel)
#print(orangel)
dha=abs(s-a)
dho=abs(t-b)
#print(dha)
#print(dho)
filtera=[]
for i in range(0,len(applel)):
    if applel[i]>0:
        filtera.append(applel[i])
filtero=[]
for i in range(0,len(orangel)):
    if orangel[i]<0:
        filtero.append(orangel[i])
#print(filtera)
#print(filtero)
ctr=0
for i in range(0,len(filtera)):
    if filtera[i]>=dha and filtera[i]<=abs(t):
        ctr+=1
print(ctr)
ctr=0
for i in range(0,len(filtero)):
    if abs(int(filtero[i]))>=dho and filtero[i]<=abs(b+s):
        ctr+=1
print(ctr)
