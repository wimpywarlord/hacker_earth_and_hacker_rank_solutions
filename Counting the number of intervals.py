x=input()
n,c=x.split()
n=int(n)
c=int(c)
#print(c)
y=input()
l=y.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
#print(l)
ctr=0
for i in  range(0,len(l)):
    for j in range(0,len(l)):
        v=[]
        if i<=j:
            for k in range(i,j+1):
                v.append(l[k])
            #print(v)
            #print(l[i]+l[j]+min(v))
            if l[i]+l[j]+min(v)<=c:
                ctr+=1
print(ctr)
        
            
        
