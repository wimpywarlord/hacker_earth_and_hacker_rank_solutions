n=int(input())
arr=[]
ctr3=1
ctr2=1
for i in range(1,n+1):
    if i%2==0:
        arr.append(3**(ctr3)*10)
        ctr3+=1
    else:
        arr.append(2**(ctr2)*10)
        ctr2+=1
#print(arr)
z=max(arr)
for i in range(0,len(arr)):
    if arr[i]==z:
        del arr[i]
        break
print(max(arr)+z+abs(z-max(arr)))
