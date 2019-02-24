t=int(input())
for i in range(0,t):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    d1={}
    d2={}
    for j in range(0,n):
        d1[x[j]]=0
    for j in range(0,n):
        d2[y[j]]=0
    for j in range(0,n):
        d1[x[j]]+=1
    for j in range(0,n):
        d2[y[j]]+=1
    d1vals=list(d1.values())
    d2vals=list(d2.values())
    d1keys=list(d1.keys())
    d2keys=list(d2.keys())
    zzz=max(d1vals)
    print(zzz)
    yyy=max(d2vals)
    print(yyy)
    print(d1vals)
    print(d2vals)
    for j in range(0,len(d1keys)):
        if d1[d1keys[j]]==zzz:
            usecom1=d1keys[j]
    for j in range(0,len(d2keys)):
        if d2[d2keys[j]]==yyy:
            usecom2=d2keys[j]
    print(usecom1)
    print(usecom2)
    if usecom1>usecom2:
        print("Rupam")
    elif usecom2>usecom1:
        print("Ankit")
    else:
        print("Tie")

