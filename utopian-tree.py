t=int(input())
for i in range(0,t):
    h=1
    n=int(input())
    if n==0:
        print(1)
    else:
        for i in range(1,n+1):
            if i%2==0:
                h+=1
            else:
                h=h*2
        print(h)
