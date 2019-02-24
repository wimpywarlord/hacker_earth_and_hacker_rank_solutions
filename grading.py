n=int(input())
for i in range(0,n):
    x=int(input())
    if x<38:
        print(x)
    else:
        z=0
        for i in range(x,101):
            if i%5==0:
                z=i
                break
        if z-x < 3:
            print(z)
        else:
            print(x)
                
                
