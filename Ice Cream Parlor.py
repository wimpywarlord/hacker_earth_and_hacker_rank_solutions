t=int(input())
for i in range(0,t):
    m=int(input())
    n=int(input())
    arr=list(map(int,input().split()))
    #print(arr)
    pos1=0
    pos2=0
    for j in range(0,n):
        for k in range(0,n):
            if j!=k:
                if arr[j]+arr[k]==m:
                    pos1=k
                    pos2=j
    print(pos1+1,end=' ')
    print(pos2+1)
