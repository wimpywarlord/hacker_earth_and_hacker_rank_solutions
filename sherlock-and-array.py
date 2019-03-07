
'''t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    use=sum(arr)
    flag=1
    for j in range(0,n):
        temp1=0
        temp2=0
        for k in range(0,j):
            temp1+=arr[k]
        for k in range(j+1,n):
            temp2+=arr[k]
        if temp1==temp2:
            print("YES")
            flag=0
            break
    if flag==1:
        print("NO")
'''        
#============================================================================

t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    i=0
    j=n-1
    s=0
    use=0
    for j in range(0,n):
        if arr[j]!=0:
            use+=1
    if use==1:
        print("YES")
    else:
        while(i!=j):
            if s>=0:
                s-=arr[j]
                j-=1
            else:
                s+=arr[i]
                i+=1
        if s==0 or n==1:
            print("YES")
        else:
            print("NO")
            
