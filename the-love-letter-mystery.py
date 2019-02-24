t=int(input())
for i in range(0,t):
    s=input()
    uses=''
    for j in range(0,len(s)//2):
        uses+=s[j]
    #print(uses)
    ans=0
    srev=s[::-1]
    if s==srev:
        ans=0
    else:
        if len(s)%2==0:
            ctr=0
            for j in range(len(s)//2,len(s)):
                for k in range(len(uses)-1,-1,-1):
                    #print(s[j])
                    print(uses[k],end=' ')
                    ans+=abs(ord(s[j])-ord(uses[k]))
                    ctr+=1
                    break
            print()
        else:
            ctr=0
            for j in range(len(s)//2+1,len(s)):
                for k in range(len(uses)-ctr,-1,-1):
                    #print(s[j])
                    print(uses[k],end=' ')
                    ans+=abs(ord(s[j])-ord(uses[k]))
                    ctr+=1
                    break
            print()
    #print(ans)
        
