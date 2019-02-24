z=input()
n,x=z.split()
n=int(n)
x=int(x)
l=list(map(int,input().split()))
#print(l)
ctr=0
ptr=0
ans=[]
for i in range(0,len(l)):
    if l[i]<=x :
        ctr+=1
        ans.append(ctr)
    elif l[i]>x:
        if ptr<=1:
            ptr+=1
        if ptr>1:
            ptr=0
            ctr=0
            break
if not ans:
    print(0)
else:
    print(max(ans))
        
