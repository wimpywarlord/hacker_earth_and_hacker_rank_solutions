t=int(input())
for i in range(0,t):
    s=input()
    d={}
    for j in range(0,len(s)):
        d[s[j]]=0
    key=list(d.keys())
    if len(key)==26:
        print("YES")
    else:
        print("NO")
    
