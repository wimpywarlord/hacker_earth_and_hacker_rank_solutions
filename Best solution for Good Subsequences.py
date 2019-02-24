mod=pow(10,9)+7
tc=int(input())
for _ in range(tc):
    s=input().strip()
    print(s)
    x=len(set(s))
    f=list(set(s))
    print(f)
    r=1
    for i in f:
        r=r*s.count(i)
    print(r%mod)
