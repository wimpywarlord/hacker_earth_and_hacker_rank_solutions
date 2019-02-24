t=int(input())
currenta=0
currentb=7
for i in range(0,t):
    n=int(input())
    if abs(n-currenta)>abs(n-currentb):
        currentb=n
        print("B")
    elif abs(n-currenta)<=abs(n-currentb):
        currenta=n
        print("A")
    
