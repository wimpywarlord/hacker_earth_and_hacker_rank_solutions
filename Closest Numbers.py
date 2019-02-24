n=int(input())
for i in range(n):
    arr=list(map(int,input().split()))
    arr.sort()
    use=[]
    usectr=0
    pair=[]
    for i in range(len(arr)):
        if i!=len(arr)-1:
            use.append([])
            use[usectr].append(arr[i])
            use[usectr].append(arr[i+1])
            pair.append(abs(arr[i]-arr[i+1]))
            usectr+=1
    #print(use)
    #print()
    #print(pair)
    #print(min(pair))
    z=min(pair)
    ans=[]
    for i in range(0,len(pair)):
        if pair[i]==z:
            ans.append(use[i][0])
            ans.append(use[i][1])
    #print(ans)
    ans.sort()
    for i in range(0,len(ans)):
        print(ans[i],end=' ')
    
