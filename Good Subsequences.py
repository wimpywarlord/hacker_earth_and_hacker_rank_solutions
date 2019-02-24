n=int(input())
for i in range(0,n):
    s=list(input())
    ans=[]
    for j in range(0,len(s)):
        ctr=0
        use=[]
        for k in range(j,len(s)):
            if s[k] not in use:
                ctr+=1
                use.append(s[k])
            else:
                ans.append(ctr)
                ctr=0
                break
        if ctr!=0:
            ans.append(ctr)
    print(ans)
        
            
            
            
