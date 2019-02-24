t=int(input())
for i in range(0,t):
    ss=input()
    s=[]
    for j in range(0,len(ss)):
        s.append(ss[j])
    print(s)
    f=[]
    for j in range(0,len(s)):
        ctr=0
        for k in range(j,len(s)):
            temp=''
            for l in range(j,len(s)-ctr):
                print(s[l],end=' ')
                temp+=s[l]
            ctr+=1
            f.append(temp)
            print()
    print(f)
    ans=0
    for j in range(0,len(f)):
        vctr=0
        for k in f[j]:
            if k=='a' or k=='A' or k=='e' or k=='E' or k=='i' or k=='I' or k=='o' or k=='O' or k=='u' or k=='U':            
                 vctr+=1
        ans+=vctr
    print(ans)
