import math
z=input()
n,k=z.split()
n=int(n)
k=int(k)
xi=input()
x=xi.split()
for i in range(0,len(x)):
    x[i]=int(x[i])
yi=input()
y=yi.split()
for i in range(0,len(y)):
    y[i]=int(y[i])
#print(x)
#print(y)
use=[]
for i in range(0,len(x)):
    use.append(((x[i])**2+(y[i])**2)**(1/2))
use.sort()
#print(use)
check=use[k-1]
#print(check)
print(math.ceil(check))
