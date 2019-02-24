t=int(input())
for i in range(0,t):
    n=int(input())
    for j in range(0,n):
        s=input()
        def defaultvalue():
            return 0
        d=defaultdict(defaultvalue)
        for k in range(0,len(s)):
            d[s[k]]+=1
        print(d)
