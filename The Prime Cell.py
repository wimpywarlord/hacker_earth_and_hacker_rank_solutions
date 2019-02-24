# mAKE A 2-D ARRAY WITH JUST A BIGGER RING OR SQUARE APPENED WITH ZEROS, AND HENCE YOU WOULD NOT NEED ANY OF THE 
# IF CONDDTIITIONSS

n=int(input())
a=[]
def prime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

for i in range(n):
    x=input()
    l=x.split()
    a.append([])
    for j in range(n):
        a[i].append(l[j])
        
for i in range(n):
    for j in range(n):
        a[i][j]=int(a[i][j])
    
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
count=0

counter=1
for i in range(n):
    for j in range(n):
        summ=0
        if 0<=i+1<n and 0<=i-1<n and 0<=j+1<n and 0<=j-1<n:
            summ=a[i+1][j]+a[i-1][j]+a[i][j+1]+a[i][j-1]
            print(counter,".")   
            counter+=1
            print("->*1")
            print(summ)
        if i+1>n  and 0<=i-1<n and 0<=j+1<n and 0<=j-1<n:
            summ=a[i-1][j]+a[i][j+1]+a[i][j-1]
            print(counter,".") 
            counter+=1
            print("->*2")
            print(summ)
        if i-1<0 and 0<=i+1<n and 0<=j+1<n and 0<=j-1<n:
            summ=a[i+1][j]+a[i][j+1]+a[i][j-1]
            print(counter,".") 
            counter+=1
            print("->*3")
            print(summ)
        if 0<=i+1<n and 0<=i-1<n and j+1>n and 0<=j-1<n:
            summ=a[i+1][j]+a[i-1][j]+a[i][j-1]
            print(counter,".") 
            counter+=1
            print("->*4")
            print(summ)
        if 0<=i+1<n and 0<=i-1<n and 0<=j+1<n and j-1<0:
            summ=a[i+1][j]+a[i-1][j]+a[i][j+1]
            print(counter,".") 
            counter+=1
            print("->*5")
            print(summ)
        if j-1<0 and i-1<0 and 0<=j+1 <n and 0<=i+1<n:
            summ=a[i+1][j]+a[i][j+1]
            print(counter,".") 
            counter+=1
            print("->*6")
            print(summ)
        if j-1<0 and i+1>n and 0<=j+1<n and 0<=i-1<n:
            summ=a[i-1][j]+a[i][j+1]
            print(counter,".")
            counter+=1
            print("->*7")
            print(summ)
        if i+1>n and j+1>n and 0<=j-1<n and 0<=i-1<n:
            summ=a[i-1][j]+a[i][j-1]
            print(counter,".") 
            counter+=1
            print("->*8")
            print(summ)
        if i-1<0 and j+1>n and 0<=j-1<n and 0<=i+1<n:
            summ=a[i+1][j]+a[i][j-1]
            print(counter,".") 
            counter+=1
            print("->*9")
        z=prime(summ)
        print(z)
        if z==True:
            count+=1
print(count)
