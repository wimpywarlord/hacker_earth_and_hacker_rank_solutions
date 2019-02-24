n=int(input())
q=int(input())
def prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
arr=list(map(int,input().split()))
arr.insert(0,0)
#print(arr)
for i in range(0,q):
    z=list(map(int,input().split()))
    #print(z)
    if z[0]==1:
        #print("#")
        for j in range(z[1],z[2]+1):
            if  arr[j]!=0 or arr[j]!=1 or arr[j]!=2:
                for k in range(arr[j]-1,2,-1):
                    #print(k,end='$')
                    #print()
                    if prime(k):
                        z=k
                        break
            arr[j]=arr[j]-z
        #print(arr)        
                
    else:
        #print("@")
        s=0
        for j in range(z[1],z[2]+1):
            s+=arr[j]
        print(s%(10**8+7))
        
    
