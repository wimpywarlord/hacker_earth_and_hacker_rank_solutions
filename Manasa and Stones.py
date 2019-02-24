t=int(input())
for i in range(0,t):
    n=int(input())
    a=int(input())
    b=int(input())
    ans=[]
    ans.append((n-1)*a)
    ans.append((n-1)*b)
    ctr=1
    while(((n-1)*max(a,b))-(ctr*abs(b-a)))>(n-1)*min(b,a):
        ans.append(((n-1)*max(a,b))-(ctr*abs(b-a)))
        ctr+=1
    p=[]
    for j in range(0,len(ans)):
        if ans[j] not in p:
            p.append(ans[j])
    p.sort()
    for j in range(0,len(p)):
        print(p[j],end=' ')
    print()
    
