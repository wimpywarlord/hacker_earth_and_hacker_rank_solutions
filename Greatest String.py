t=int(input())
l=['a','e','i','o','u']
for i in range(0,t):
    ss=input()
    s=[]
    for j in range(0,len(ss)):
        s.append(ss[j])
    n=int(input())
    ctr=0
    for j in range(0,len(s)):
        if ctr==n:
            break
        if s[j] in l:
            s[j]=chr(ord(s[j])+1)
            ctr+=1
        
    ans="".join(s)
    print(ans)
