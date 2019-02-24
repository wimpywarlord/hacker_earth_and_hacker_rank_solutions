t=int(input())
for i in range(0,t):
    n,r=map(int,input().split())
    l=list(map(int,input().split()))
    #print(l)
    max=0
    ctr=0
    for j in range(0,len(l)):
        if l[j]>max:
            ctr+=1
            max=l[j]
    print(ctr*r)
