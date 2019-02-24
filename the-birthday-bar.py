n=int(input())
for i in range(0,n):
    x=input()
    l=x.split()
    z=input()
    date,month=z.split()
    date=int(date)
    month=int(month)
    for j in range(0,len(l)):
        l[i]=int(l[i])
    v=[]
    ptr=0
    for j in range(0,len(l)):
        ctr=0
        for k in range(j,len(l)):
            v.append([])
            for m in range(j,len(l)-ctr):
                #print(l[m],end='')
                v[ptr].append(l[m])
            ptr+=1
            #print()
            ctr+=1
    #print(v)
    ss=[]
    for j in range(0,len(v)):
        for k in range(0,len(v[j])):
            v[j][k]=int(v[j][k])
                       
    for j in range(0,len(v)):
        su=0
        for k in range(0,len(v[j])):
            su+=v[j][k]
        ss.append(su)
    #print(ss)
    ans=0
    for j in range(0,len(ss)):
        if len(v[j])==month and ss[j]==date:
            ans+=1
    print(ans)
            
    
