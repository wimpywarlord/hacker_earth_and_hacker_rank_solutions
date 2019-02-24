t=int(input())
toffe=0
for i in range(0,t):
    x=input()
    r,h=x.split()
    r=float(r)
    h=float(h)
    peri=2*(3.141592653589793238462643)*r
    cap=100*h
    if cap>=peri:
        toffe+=1
    elif cap<peri:
        pass
print(toffe)
        
