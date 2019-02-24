v=input("Enter N:")
vv=v.split()
for i in range(0,len(vv)):
    vv[i]=int(vv[i])
for t in range(0,len(vv)):
    if t==0:
        pass
        n=vv[t]
        n=2*n-1
        x=n//2
        y=n//2
        mat=[]
        for i in range(0,n):
            mat.append([])
            for j in range(0,n):
                mat[i].append(0)
        mat[x][y]=1
        dist=0
        for i in range(0,n):
            for j in range(0,n):
                dist=max(abs(x-i),abs(y-j))
                mat[i][j]=dist+1
        for i in range(0,n):
            for j in range(0,n):
                print(mat[i][j],end='')
            print()
    else:
        print("Enter N:",end='')
        n=vv[t]
        n=2*n-1
        for k in range(0,vv[t]):
            print(vv[t],end='')
        x=n//2
        y=n//2
        mat=[]
        for i in range(0,n):
            mat.append([])
            for j in range(0,n):
                mat[i].append(0)
        mat[x][y]=1
        dist=0
        for i in range(0,n):
            for j in range(0,n):
                dist=max(abs(x-i),abs(y-j))
                mat[i][j]=dist+1
        for i in range(0,n):
            for j in range(0,n):
                print(mat[i][j],end='')
            print()

        
