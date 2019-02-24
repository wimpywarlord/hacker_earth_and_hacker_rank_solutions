t=int(input())
for i in range(0,t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    flag=0
    for j in range(0,len(l)):
        if l[j]<k:
            flag=1
            break
    if flag==0:
        print(0)
    else:
        print(k-min(l))
