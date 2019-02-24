t=int(input())
for i in range(0,t):
    s=input()
    l=[]
    ans=0
    for j in range(0,len(s)):
        if s[j] not in l:
            ans+=1
            l.append(s[j])
    print(ans)
        
        
