t=int(input())
for i in range(0,t):
    n,k=map(int,input().split())
    #print(n)
    #print(k)
    l=list(map(int,input().split()))
    #print(l)
    #b=list(l)
    #print(b)
    ans=[]
    for j in range(0,len(l)):
        ans.append(0)
    ctr=0
    ptr=0
    if k>len(l):
        k=k%len(l)
    for j in range(0,len(l)):
        if j<k:
            ans[j]=l[len(l)-k + ctr]
            ctr+=1
        elif j>=k:
            ans[j]=l[ptr]
            ptr+=1
    #print(ans)
    for j in range(0,len(ans)):
        print(ans[j],end=' ')
            
