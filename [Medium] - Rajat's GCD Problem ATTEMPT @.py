def hcfcal(m,n):
    if(n==0):
        return m
    else:
        return hcfcal(n,m%n)
t=int(input())
for x in range(t):
    x,y,n=map(int,input().split())
    m=hcfcal(x+y,abs(x-y))
    print(m%1000000007)
