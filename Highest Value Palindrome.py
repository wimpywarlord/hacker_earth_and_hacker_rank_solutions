n,k=map(int,input().split())
if n==1 and k>0:
    print(9)
else:
    s=list(input())
    pc=0
    for i in range(0,n//2):
        if s[i]!=s[n-1-i]:
            pc=1
            break
    if pc==0 and k>0:
        usectr=int(k)
        temp=0
        #print("*")
        while usectr>=2:
            if s[temp]!='9' :
                s[temp]='9'
                usectr-=1
            if s[n-1-temp]!='9' :     
                s[n-1-temp]='9'
                usectr-=1
            temp+=1
        print("".join(s))
    else:
        ctr=0
        use=[]
        for i in range(0,n//2):
            #print(s[i],s[n-i-1])
            if s[i]!=s[n-1-i]:
                use.append(s[i])
                use.append(s[n-i-1])    
                ctr+=2
        ctr-=1
        if ctr>k:
            print("-1")
        else:
            for i in range(0,n//2):
                #print(s[i],s[n-i-1])
                if s[i]!=s[n-1-i]:
                    s[i]=max(use)
                    s[n-1-i]=max(use)
                    k-=2
            print(s)
            if k>=2:
                print(s)
                print("$")
                print(k)
                temp=0
                while k>=2:
                    print(s[temp])
                    if s[temp]!='9' :
                        s[temp]='9'
                        k-=1
                    if s[n-1-temp]!='9' :     
                        s[n-1-temp]='9'
                        k-=1
                    temp+=1
            print("".join(s))
