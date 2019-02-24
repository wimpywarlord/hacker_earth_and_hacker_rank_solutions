t=int(input())
for i in range(0,t):
    arr=list(map(int,input().split()))
    #print(arr)
    z=arr[0]
    #print(z)
    final=[]
    del arr[0]
    if z%arr[0]==0:
        final.append(z//arr[0])
    if z%arr[1]==0:
        final.append(z//arr[1])
    if z%arr[2]==0:
        final.append(z//arr[2])
    use=[]
    usectr=0
    for j in range(0,len(arr)):
        for k in range(0,len(arr)-j):
            use.append([])
            for m in range(j,len(arr)-k):
                #print(arr[m],end=' ')
                use[usectr].append(arr[m])
            usectr+=1
            #print()
    #print(use)
    ss=[]
    ans=0
    ans=0
    for j in range(0,len(use)):
        q=0
        for k in range(0,len(use[j])):
            q+=use[j][k]
        if q==z:
            #print(use[j])
            final.append(len(use[j]))
            ans+=len(use[j])
    print(max(final))
