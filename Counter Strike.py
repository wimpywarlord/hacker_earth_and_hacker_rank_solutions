t=int(input())
for i in range(0,t):
    x=input()
    n,m,d=x.split()
    n=int(n)
    m=int(m)
    d=int(d)
    location=[]
    for j in range(0,n):
        location.append([])
        y=input()
        x1,y1=y.split()
        x1=int(x1)
        y1=int(y1)
        location[j].append(x1)
        location[j].append(y1)
    print(location)
    targets=[]
    for j in range(0,m):
        targets.append([])
        z=input()
        x2,y2=z.split()
        x2=int(x2)
        y2=int(y2)
        targets[j].append(x2)
        targets[j].append(y2)
    print(targets)
    ctr=0
    for j in range(0,len(location)):
        for k in range(0,len(targets)):
            if (((targets[k][0]-location[j][0])**2)+((targets[k][1]-location[j][1])**2))**(1/2)<=d:
                 ctr+=1
        if ctr==len(targets):
            break
    if ctr>m//2:
        print("YES")
    else:
        print("NO")
                
                                
