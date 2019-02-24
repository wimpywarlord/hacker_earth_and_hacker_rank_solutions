t=int(input())
from collections import defaultdict 
def defaultvalue():
    return 0
d=defaultdict(defaultvalue)
for i in range(0,t):
    s=input()
    if i==0:
        for j in range(0,len(s)):
            d[s[j]]+=1
        temp=list(s)
    else:
        for j in range(0,len(s)):
            if s[j] not in temp:
                d[s[j]]=0
        key=list(d.keys())
        for j in range(0,len(key)):
            if key[j] not in s:
                d[key[j]]=0
        temp=list(s)
val=list(d.values())
ans=0
for i in range(0,len(val)):
    if val[i]!=0:
        ans+=1
print(ans)
    
    
    
        
    
