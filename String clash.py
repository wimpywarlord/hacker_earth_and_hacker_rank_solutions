ss1=input()
ss2=input()
s1=[]
s2=[]
for i in range(0,len(ss1)):
    s1.append(ss1[i])
for i in range(0,len(ss2)):
    s2.append(ss2[i])
new=[]
from collections import defaultdict
def defaultvalue():
    return 0
d=defaultdict(defaultvalue)
for i in range(0,len(s1)):
    d[s1[i]]+=1
for i in range(0,len(s2)):
    d[s2[i]]+=1
ans=0
k=list(d.keys())
#print(k)
#print(d)
for i in range(0,len(k)):
    ans+=d[k[i]]//2
print(ans*2+1)

