t=int(input())
for i in range(0,t):
    n=int(input())
    m=int(input())
    arr=[]
    for j in range(0,n):
        arr.append(j+1)
    print(arr)
    ctr=m
    while len(arr)>1:
        del arr[m-1::m]
    print(arr)
            
            
    
            
            
        
        
    
        

