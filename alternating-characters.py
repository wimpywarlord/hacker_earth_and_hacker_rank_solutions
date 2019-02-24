t=int(input())
for i in range(0,t):
    s=list(input())
    ans=0
    for j in range(0,len(s)):
        if j!=len(s)-1:
            if s[j]==s[j+1]:
                ans+=1
    print(ans)
