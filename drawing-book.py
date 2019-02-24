n=int(input())
p=int(input())
if p==1:
    print(0)
elif p==n:
    print(0)
elif n%2==0 and p==n-1:
    print(1)
else:
    z=p//2
    w=(n-p)//2
    if z>=w:
        print(w)
    if z<w:
        print(z)
    
