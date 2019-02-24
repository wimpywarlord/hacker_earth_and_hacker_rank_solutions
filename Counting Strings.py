t=int(input())
for i in range(0,t):
    ptr=0
    x=input()
    v=[]
    for j in range(0,len(x)):
        ctr=0
        for k in range(j,len(x)):
            v.append([])
            for l in range(j,len(x)-ctr):
                print(x[l],end='')
                v[ptr].append(x[l])
            ptr+=1
            ctr+=1
            print()
    print(v)
    ans=0
    for m in range(0,len(v)):
        flag=0
        for n in range(0,len(v[m])):
            if v[m][n]=='a' or v[m][n]=='z':
                flag=1
        if flag==1:
            ans+=1
    print(ans)
            
