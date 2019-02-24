t=int(input())
for i in range(0,t):
    q=input()
    x,y,z=q.split()
    x=int(x)
    y=int(y)
    z=int(z)
    if abs(z-x)>abs(z-y):
        print("Cat B")
    elif abs(z-x)<abs(z-y):
        print("Cat A")
    elif abs(z-x)==abs(z-y):
        print("Mouse C")
