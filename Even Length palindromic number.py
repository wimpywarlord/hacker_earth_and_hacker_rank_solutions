t=int(input())
for i in range(0,t):
    x=int(input())
    f=str(x)
    l = "".join(reversed(f))
    print(f)
    print(l)
    palin=f+l
    print(palin)
    d={}
    for j in range(0,len(palin)):
        d[palin[j]]=0
    for j in range(0,len(palin)):
        d[palin[j]]+=1
    print(d)
    val=list(d.values())
    print(val)
    se=max(val)
    key=list(d.keys())
    print(key)
    ans=[]
    for i in range(0,len(key)):
        if d[key[i]]==se:
            ans.append(key[i])
    print(ans)
    final=min(ans)
    print(final)
