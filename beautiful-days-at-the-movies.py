z=input()
i,j,k=z.split()
i=int(i)
j=int(j)
k=int(k)
ctr=0
for p in  range(i,j+1):
    a=str(p)
    b=a[::-1]
    #print(a)
    b=b.lstrip('0')
    #print(b)
    ans=abs(int(b)-int(a))
    if ans%k==0:
        
        ctr+=1
print(ctr)
