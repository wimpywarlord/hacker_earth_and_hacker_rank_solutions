t=int(input())
for i in range(0,t):
    x=input()
    n1,n2=x.split()
    n1=n1[::-1]
    n2=n2[::-1]
    n1=int(n1)
    n2=int(n2)
    #print(n1,n2)
    ans=n1+n2
    ans=str(ans)
    ans=ans[::-1]
    final=''
    flag=0
    for i in range(0,len(ans)):
        if ans[i]=='0' and flag==0:
            pass
        else:
            flag=1
            final+=ans[i]
    print(final)
