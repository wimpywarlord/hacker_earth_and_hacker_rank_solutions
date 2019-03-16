'''
n,swaps=map(int,input().split())
arr=list(map(int,input().split()))
arr_copy=sorted(arr,reverse=True)
#print(arr_copy)
ctr=0
for i in range(n):
    if ctr==swaps:
        break
    else:
        pos=0
        for j in range(0,len(arr)):
            if arr[j]==arr_copy[0]:
                pos=j
                del arr_copy[0]
                break
        #print(arr[pos],arr[i])
        if pos==i:
            pass
        else:
            arr[pos],arr[i]=arr[i],arr[pos]
            ctr+=1
    if arr==arr_copy:
        break
print(*arr)
'''
n, k = [int(v) for v in input().split()]
a = [int(v) for v in input().split()]
d = {}
for idx, v in enumerate(a):
    d[v] = idx
for i, maxValue in enumerate(range(n, 0, -1)):
    if maxValue > a[i]:
        oldValue = a[i]
        newIndex = d[maxValue]
        a[i], a[newIndex] = a[newIndex], a[i]
        d[oldValue] = newIndex
        d[maxValue] = i
        k -= 1
    if k == 0:
        break
print(*a)
            
        
                    
    
