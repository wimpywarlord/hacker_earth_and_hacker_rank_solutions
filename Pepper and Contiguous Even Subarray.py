t=int(input())
bigflag=0
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i):
            use=[]
            for k in range(i,len(arr)-j):
                use.append(arr[k])
                #print(arr[k],end=' ')
            flag=0
            for m in range(0,len(use)):
                if use[m]%2!=0:
                    flag=1
            if flag==0:
                print(len(use))
                bigflag=1
            if bigflag==1:
                break
        if bigflag==1:
            break
    if bigflag==1:
        break
if bigflag==0:
    print(-1)
    
            
                
                
