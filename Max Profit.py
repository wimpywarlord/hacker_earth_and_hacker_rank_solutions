n=int(input())
x=input()
s=x.split()
for i in range(0,len(s)):
    s[i]=int(s[i])
rrr=max(s)
t=0
for j in range(0,len(s)):
    if s[j]==rrr:
        t=j
new=[]
for k in range(0,t):
    new.append(s[k])

print(rrr-min(new))
