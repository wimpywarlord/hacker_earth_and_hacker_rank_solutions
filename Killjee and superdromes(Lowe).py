t=int(input())
s=input()
a=s.split()
e=s.split()
for i in range(0,len(a)):
    a[i]=int(a[i])
print(a)
for i in range(0,len(a)):
    v=[]
    w=[]
    ctr=0
    for j in range(1,a[i]+1):
        v.append(j)
        w.append(j)
    yyy=[]
    uuu=[]
    for k in v:
        d=[]
        zzz=[]
        while k>0:
            g=k%10
            d.append(g)
            k=k//10
        print(d)
        for kk in range(len(d)-1,-1,-1):
            zzz.append(d[kk])
        print(zzz)
        if d==zzz:
            print("*")
            yyy.append(1)
        else:
            print("&")
            yyy.append(0)
    for h in w:
        b=[]
        ccc=[]
        while h>0:
            r=h%2
            b.append(r)
            h=h//2
        for jj in range(len(b)-1,-1,-1):
            ccc.append(b[jj])
        print(ccc)
        if ccc==b:
            print("#")
            uuu.append(1)
        else:
            print("@")
            uuu.append(0)
    print(uuu)
    print(yyy)
    for i in range(0,len(uuu)):
        if uuu[i]==1 and yyy[i]==1:
            ctr+=1
    print(ctr)
