for i in range(int(input())):
    n,kkk=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    mat=[]
    for j in range(0,len(a)):
        mat.append([])
        for k in range(0,len(b)):
            mat[j].append(a[j]+b[k])
    #print(mat)
    mainflag=0
    use=[]
    for j in range(0,len(mat)):
        c=0
        for k in range(0,len(mat[j])):
            if mat[j][k]>=kkk:
                c+=1
        use.append(c)
    #print(use)
    use.sort()
    flag=0
    for i in range(0,len(use)):
        if use[i]<i+1:
            print("NO")
            flag=1
            break
    if flag==0:
        print("YES")
            
                
