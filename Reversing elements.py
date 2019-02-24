from sys import maxsize 
def maxSubArraySum(a,size):  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(0,size): 
        max_ending_here += a[i] 
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
    print ((max_so_far)) 

x=input()
n,q=x.split()
n=int(n)
q=int(q)
y=input()
arr=y.split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
copy=arr.copy()
for i in range(0,q):
    for j in range (0,len(copy)):
        arr[j]=copy[j]
    #print(arr)
    z=input()
    l,r=z.split()
    l=int(l)
    r=int(r)
    ctr=0
    for j in range(l-1,r):
        k=r-1-ctr
        #print(copy[k])
        arr[j]=copy[k]
        ctr+=1
    #print(arr)
    #print() 
    maxSubArraySum(arr,len(arr))
   
    
    
