t=int(input())
for i in range(0,t):
    n=int(input())
    z=input()
    l=z.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    l.sort()
    #print(l)
    for j in range(0,len(l)):
        for k  in range(0,len(l)):
            if l[j]==l[k]+1 or l[j]==l[k]-1:
                l[k]=-100000
    ans=0
    for j in range(0,len(l)):
        if l[j]!=-100000:
            ans+=1
    print(ans)
