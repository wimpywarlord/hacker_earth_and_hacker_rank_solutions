t=int(input())
for i in range(0,t):
    n=int(input())
    a=input()
    l=a.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    #print(l)
    v=[]
    b=0
    for j in range(0,len(l)):
        ctr=0
        for k in range(j,len(l)):
            v.append([])
            for m in range(j,len(l)-ctr):
                #print(l[m],end=' ')
                v[b].append(l[m])
            b+=1 
            ctr+=1
            #print()
    #print(v)
    q=[]
    for j in range(0,len(v)):
        if len(v[j])>=2:
            q.append(v[j])
    #print(q)
    w=[]
    for j in range(0,len(q)):
        summ=0
        for k in range(0,len(q[j])):
            summ+=q[j][k]
        w.append(summ)
    print(min(w))
        
