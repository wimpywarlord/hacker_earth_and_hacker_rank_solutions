n=int(input())
a=input()
arr=a.split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
#print(arr)

check=0
while len(arr)>0:
    xx=len(arr)
    print(len(arr))
    z=min(arr)
    for i in range(0,xx):
        arr[i]=arr[i]-z
    #print(arr)
    for j in range(0,xx):
        yy=len(arr)
        for k in range(0,yy):
            if arr[k]==0:
                del arr[k]
                break
    

    
    
            
