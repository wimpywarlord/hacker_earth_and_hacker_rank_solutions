n=input()
zzz=len(n)
use=[]
for i in range(0,len(n)):
    for j in range(0,int(n[i])):
        use.append(10**(len(n)-i-1))
#print(use)
d={}
for i in range(0,len(use)):
    d[use[i]]=0
for i in range(0,len(use)):
    d[use[i]]+=1
#print(d)
val=list(d.values())
#print(val)
ans=0
mat=[]
while len(val)>0:
    for i in range(len(val)):
        val[i]=val[i]-1
    ans=ans+1
    for i in range(len(val)):
        if val[i]!=0:
            mat.append(val[i])
    val.clear()
    for i in range(len(mat)):
        val.append(mat[i])
    mat.clear()
print(ans)
