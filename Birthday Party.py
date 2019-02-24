t=int(input())
for i in range(0,t):
    x=input()
    n,m=x.split()
    n=int(n)
    m=int(m)
    if m%n==0:
        print("Yes")
    else:
        print("No")
