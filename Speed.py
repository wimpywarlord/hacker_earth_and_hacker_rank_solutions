t=int(input())
for i in range(0,t):
    n=int(input())
    s=input()
    l=s.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    ans=1
    #print(l)
    for j in range(0,len(l)):
        if j!=len(l)-1:
            if l[j]<l[j+1]:
                l[j+1]=l[j]
            else:
                ans+=1
    print(ans)
    #print(l)
