t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    #print(arr)
    ctr=0
    use=[]
    for j in range(0,n):
        use.append([])
        for k in range(0,j):
            ss1=0
            for l in range(k+1,j):
                ss1+=arr[l]
            #print("*")
            use[ctr].append(ss1)
        ptr=0
        for k in range(j+1,n):
            ss2=0
            for l in range(j+1,n-1-ptr):
                ss2=ss2+arr[l]
                #print(arr[l])
                #print(ss2)
            ptr+=1
            #print("@")
            use[ctr].append(ss2)
        ctr+=1
    ans=[]
    #print(use)
    for j in range(0,len(arr)):
        temp=[]
        for k in range(0,len(arr)):
            if j!=k:
                temp.append(arr[k])
        #print(temp)
        temp.reverse()
        temp[0],temp[1]=temp[1],temp[0]
        ansctr=0
        for k in range(0,len(temp)):
            if temp[k]>=use[j][k]:
                ansctr+=1
                #print(temp[k],use[j][k])
        ans.append(ansctr)
            
    print(ans)
                
    
                    
                
