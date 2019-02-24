t=int(input())
for i in range(0,t):
    n=int(input())
    x=input()
    l=x.split()
    copy=l.copy()
    for j in range (0,n):
        l[j]=int(l[j])
    f=[]
    for j in range(0,n):
        v=[]
        if l[j]==0:
            v.append(0)
        while l[j]>0:
            p=l[j]%10
            v.append(p)
            l[j]=l[j]//10
        f.append(v)
    print(f)
    ctrl=[]
    for j in range(0,len(f)):
        ctr=0
        for k in range(0,len(f[j])):
            if f[j][k]==1:
                ctr+=2
            if f[j][k]==2:
                ctr+=5
            if f[j][k]==3:
                ctr+=5
            if f[j][k]==4:
                ctr+=4
            if f[j][k]==5:
                ctr+=5
            if f[j][k]==6:
                ctr+=6
            if f[j][k]==7:
                ctr+=3
            if f[j][k]==8:
                ctr+=7
            if f[j][k]==9:
                ctr+=6
            if f[j][k]==0:
                ctr+=6
        ctrl.append(ctr)
    #print(ctrl)
    ans=min(ctrl)
    #print(ans)
    for j in range(0,len(ctrl)):
        if ctrl[j]==ans:
            print(copy[j])
            break
                
            
            
            
