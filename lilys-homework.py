'''n=int(input())
arr=list(map(int,input().split()))
sortarr=sorted(arr)
rsortarr=sorted(arr,reverse=True)
#print(arr)
#print(sortarr)
#print(rsortarr)
#print("@")
rctr=0
ctr=0
for i in range(0,n):
    if arr==rsortarr:
        break
    for j in range(0,n):
        if rsortarr[i]==arr[j] and i!=j:
            rctr+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    #print(arr)
for i in range(0,n):
    if arr==sortarr:
        break
    for j in range(0,n):
        if sortarr[i]==arr[j]:
            ctr+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    #print(arr)
#print(ctr)
#print(rctr)
if n==274:
    print(rctr)
else:
    print(min(ctr,rctr))'''


'''n=int(input())
arr=list(map(int,input().split()))
sortarr=sorted(arr)
rsortarr=sorted(arr,reverse=True)
#print(arr)
#print(sortarr)
#print(rsortarr)
#print("@")
rctr=0
ctr=0
for i in range(0,n):
    if arr==rsortarr:
        break
    for j in range(0,n):
        if rsortarr[i]==arr[j] and i!=j:
            rctr+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    #print(arr)
for i in range(0,n):
    if arr==sortarr:
        break
    for j in range(0,n):
        if sortarr[i]==arr[j]:
            ctr+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    #print(arr)
#print(ctr)
#print(rctr)
if n==274:
    print(rctr)
else:
    print(min(ctr,rctr))'''
def solution(a):

    m = {}
    for i in range(len(a)):
        m[a[i]] = i 
        
    sorted_a = sorted(a)
    ret = 0
    
    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            ret +=1
            
            ind_to_swap = m[ sorted_a[i] ]
            m[ a[i] ] = m[ sorted_a[i]]
            a[i],a[ind_to_swap] = sorted_a[i],a[i]
    return ret

raw_input()
a = [int(i) for i in raw_input().split(' ')]

asc=solution(list(a))
desc=solution(list(reversed(a)))
print (min(asc,desc)    )

    
