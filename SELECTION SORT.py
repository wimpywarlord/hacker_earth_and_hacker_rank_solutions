t=int(input())
for i in range(0,t):
    x=input()
    nob,maxp=x.split()
    nob=int(nob)
    maxp=int(maxp)
    y=input()
    l=y.split()
    for j in range(0,nob):
        l[j]=int(l[j])
    print(l)
