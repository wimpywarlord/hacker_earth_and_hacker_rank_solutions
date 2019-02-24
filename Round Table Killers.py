y=input()
n,k,x=y.split()
n=int(n)
k=int(k)
x=int(x)
l=[]
for i in range(1,n+1):
    l.append(i)
print(l)
while True:
    g=x%k
    print(g,"!")
    ind=l.index(x)+1
    print(ind,"@")
    if ind+g<=len(l):
        for j in range(ind+1,ind + g+1):
            l[j-1]=-1
        x=l[ind+g]
    if ind+g>len(l):
        new=(ind+g)%len(l)
        print(new,"#")
        for j in range(ind+1,len(l)+1):
            l[j-1]=-1
        for  j in range(0,new+1):
            l[j-1]=-1
        x=l[new]
    ctr=0
    for i in range(0,len(l)):
        if l[i]!=-1:
            ctr+=1
    if (x%k)>=ctr:
        break    
print(l)
print(x)
