s1=input()
s2=input()
from collections import defaultdict
d1 = defaultdict(int)
d2=  defaultdict(int)
for i in range(0,len(s1)):
    d1[s1[i]]+=1
for i in range(0,len(s2)):
    d2[s2[i]]+=1
vald1=list(d1.values())
vald2=list(d2.values())
keyd1=list(d1.keys())
keyd2=list(d2.keys())
ans=0
for i in range(0,len(keyd1)):
    flag=0
    for j in range(0,len(keyd2)):
        if keyd1[i]==keyd2[j]:
            flag=1
            ans+=abs(vald1[i]-vald2[j])
    if flag==0:
        ans+=vald1[i]
    #print(ans)
for i in range(0,len(keyd2)):
    flag=0
    for j in range(0,len(keyd1)):
        if keyd2[i]==keyd1[j]:
            flag=1
    if flag==0:
        ans+=vald2[i]
#print(d1)
#print(d2)
print(ans)
