t=int(input())
for i in range(0,t):
    zz=input()
    z=[]
    for j in range(0,len(zz)):
        z.append(zz[j])
    d={}
    for j in range(0,len(z)):
        d[z[j]]=0
    for j in range(0,len(z)):
        d[z[j]]+=1
        if (ord(z[j])-96+d[z[j]]+13-1)>26:
            z[j]=chr(96+(ord(z[j])-96+13+d[z[j]]-1)%26)
        else:
            z[j]=chr(ord(z[j])+13+d[z[j]]-1)
    q=''
    for j in range(0,len(z)):
        q+=z[j]
    print(q)
