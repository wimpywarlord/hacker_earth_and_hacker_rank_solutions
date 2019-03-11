t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    score=[]
    mm=0
    for j in range(0,n):
        ss=0
        use=arr[j]
        for k in range(0,n):
            if arr[k]<arr[j]:
                if mm<ss:
                    mm=ss
                ss=0
            else:
                ss+=arr[j]
        score.append(max(ss,mm))
    #print(score)
    print(max(score))
        
            
        
