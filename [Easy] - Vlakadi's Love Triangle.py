n=int(input())
d={}
z=[]
ctr=0
for i in range(0,n):
    z.append([])
    a,b=map(int,input().split())
    z[ctr].append(a)
    z[ctr].append(b)
    d[a]=0
    d[b]=0
    ctr+=1
#print(z)
key=list(d.keys())
for i in range(0,len(key)):
    temp=[]
    for j in range(0,len(z)):
        for k in range(0,len(z[j])):
            if z[j][k]==key[i]:
                if k==0:
                    temp.append(z[j][1])
                if k==1:
                    #print("&")
                    temp.append(z[j][0])
    d[key[i]]=temp
ans=0
fl=list(d.values())
for i in range(0,len(fl)):
    if len(fl[i])!=1:
        ans+=((((len(fl[i]))*(len(fl[i])+1))//2)-len(fl[i]))
#print(d)
print(ans)
