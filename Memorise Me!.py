n=int(input())
arr=list(map(int,input().split()))
d1={}
for i in range(0,n):
    d1[arr[i]]=0
for i in range(0,n):
    d1[arr[i]]+=1
q=int(input())
for i in range(0,q):
    z=int(input())
    try:
        print(d1[z])
    except:
        print("NOT PRESENT")
    
    
