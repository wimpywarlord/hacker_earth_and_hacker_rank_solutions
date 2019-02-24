n=int(input())
l=list(map(int,input().split()))
from sys import maxsize
usel=[]
usescore=0
ctr=0
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
    global usescore
    global ctr
    usescore=max_so_far
    usel.append([])
    for i in range(start,end+1):
        usel[ctr].append(l[i])
        l[i]=0
    #print(l)
    while True:
        flag=0
        for i in range(0,len(l)):
            if l[i]==0:
                flag=1
                del(l[i])
                break
        if flag==0:
            break
        
    ctr+=1
    #print(l)
if max(l)<0:
    print(0)
else:
    while True :
        if len(l)==0:
            break
        maxSubArraySum(l,len(l))
    #print(usel)
    s=sum(usel[0])
    final=[]
    final.append(s)
    for i in range(1,len(usel)):
        final.append((s+sum(usel[i]))/(i+1))
    #print(final)
    z=max(final)
    if z<0:
        print(0)
    else:
        for i in range(len(final)-1,-1,-1):
            if final[i]==z:
                print(final[i],i+1)
                break
            
