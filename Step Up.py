t=int(input())
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return 1
    return 0
        
for i in range(0,t):
    z=input()
    x,y=z.split()
    x=int(x)
    y=int(y)
    count=0
    for j in range(x,y+1):
        if isprime(j)==1:
            print(j)
            count+=1
    print(count)
