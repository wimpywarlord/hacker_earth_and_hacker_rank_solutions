t=int(input())
for i in range(0,t):
    n=int(input())
    ss=input()
    s=[]
    for j in range(0,len(ss)):
        s.append(ss[j])
    d={}
    for j in range(0,len(s)):
        d[s[j]]=0
    for j in range(0,len(s)):
        if s[j]!='_':
            d[s[j]]+=1
    if len(d)==1 and d[s[0]]!=1:
        print("YES")
    else:
        #print(d)
        val=list(d.values())
        flag=0
        for j in range(0,len(val)):
            if val[j]==1:
                flag=1
        ctr=0
        for j in range(0,len(s)):
            if s[j]=='_':
                ctr+=1
        
        for j in range(0,len(s),2):
            if j!=len(s)-1:
                s[j]=ord(s[j])^ord(s[j+1])
                s[j+1]=s[j]
        gg=0
        for j in range(0,len(s)):
            if s[j]!=0:
                gg=1
        #print(s)
        if ctr==0 and gg==1 :
            flag=1
        if flag==1:
            print("NO")
        else:
            print("YES")
        
