n=int(input())
ctr=0
for i in range(0,n):
    ctr+=1
    d={}
    s=input()
    for j in range(0,len(s)):
        d[s[j]]=0
    for j in range(0,len(s)):
        d[s[j]]+=1
    print(d)
    if len(d)<3:
        print(ctr,"->","Not OK")
    else:   
        check=[]
        c=[]
        b=d.keys()
        for i in b:
            c.append(i)
        print(c)
        for i in range(0,d[c[0]]):
            check.append(c[0])
        print(check)
        check="".join(check)
        if check not in s:
            print(ctr,"->","Not OK")
        else:
            flag=0
            for j in range(0,len(d)):
                if d[c[j]]!=d[c[0]]:
                    flag=1
            if flag==0:
                print(ctr,"->","OK")
            else:
                print(ctr,"->","Not OK")
