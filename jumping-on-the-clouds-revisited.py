z=input()
e=100
n,k=z.split()
n=int(n)
k=int(k)
#print(n)
#print(k)
y=input()
l=y.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
#print(l)
pos=0
for i in range(k,len(l),k):
    if l[i]==0:
        e=e-1
        #print("%")
    elif l[i]==1:
        e=e-1-2
        #print("#")
    pos=i
#print(pos)
if pos+k>=len(l):
    if l[(i+k)%n]==0:
        e=e-1
    elif l[(i+k)%n]==1:
        e=e-1-2
print(e)
        
