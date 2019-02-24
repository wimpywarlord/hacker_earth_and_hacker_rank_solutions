t=int(input())
for i in range(0,t):
    z=input()
    n,m=z.split()
    n=int(n)
    m=int(m)
    if n==m or n==2 and m==4 or n==4 and m==2:
        print("YES")
    else:
        print("NO")
