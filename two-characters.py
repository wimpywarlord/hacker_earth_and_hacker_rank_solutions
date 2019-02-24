n=int(input())
s=list(input())
d={}
for i in range(0,len(s)):
    d[s[i]]=0
for i in range(0,len(s)):
    d[s[i]]+=1
print(d)
    
