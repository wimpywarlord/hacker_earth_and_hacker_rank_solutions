n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
ans=0
if len(l1)>=len(l2):
    l1.sort()
    l2.sort()
    #print("#")
    #print(l1)
    #print(l2)
    if max(l2)<max(l1):
        print("#")
        for i in range(0,len(l2)):
            if l1[i]<l2[i]:
                
                #print(l2[i],"-",l1[i])
                ans+=l2[i]-l1[i]
    else:
        print("$")
        z=max(l2)
        for i in range(0,len(l1)):
            ans+=z-l1[i]
if len(l1)<len(l2):
    l1.sort()
    l2.sort(reverse=True)
    if max(l2)<max(l1):
        print("*")
        for i in range(0,len(l1)):
            if l1[i]<l2[i]:
                #print(l2[i],"-",l1[i])
                ans+=l2[i]-l1[i]
    else:
        print("!")
        z=max(l2)
        for i in range(0,len(l1)):
            ans+=z-l1[i]
print(ans)
