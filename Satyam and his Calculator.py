t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.insert(0,0)
    print(arr)
    q=int(input())
    for j in range(0,q):
        z=list(map(int,input().split()))
        if z[0]==1:
            arr[z[1]]=z[2]
            print(arr)
        else:
            temp=[]
            print(z[1],z[2],"*")
            for k in range(z[1],z[2]+1):
                temp.append(arr[k])
            print(temp)
            nor=sorted(temp)
            rev=sorted(temp,reverse=True)
            d={}
            for k in range(0,len(temp)):
                d[temp[k]]=0
            for k in range(0,len(temp)):
                d[temp[k]]+=1
            if len(d)==1:
                print(-1)
            elif temp==nor:
                print(0)
            elif temp==rev:
                print(1)
            else:
                print(-1)
                
            
            
        
