t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    use=[]
    ptr=0
    for j in range(0,n):
        use.append([])
        for k in range(0,j):
            ss=0
            for m in range(k+1,j):
                ss+=arr[m]
            use[ptr].append(ss)
        ctr=0
        for k in range(j+1,n):
            ss=0
            for m in range(j+1,j+1+ctr):
                ss+=arr[m]
            ctr+=1
            use[ptr].append(ss)
        ptr+=1
    #print(use)
    ans=[]
    for j in range(0,n):
        temp=[]
        for k in range(0,n):
            if j!=k:
                temp.append(arr[k])
        #print(temp)
        ansctr=0
        for k in range(0,n-1):
            if temp[k]>=use[j][k]:
                ansctr+=1
        ans.append(ansctr)
    for i in range(0,n):
        print(ans[i],end=' ')
    print()
    #print(ans)
