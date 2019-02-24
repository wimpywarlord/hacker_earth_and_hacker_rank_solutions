s=input()
from collections import defaultdict
d1=defaultdict(int)
for i in range(0,len(s)):
    d1[s[i]]+=1
#print(d1)
d1val=list(d1.values())
ctr=0
for i in range(0,len(d1val)):
    if d1val[i]%2!=0:
        ctr+=1
if ctr>1:
    print("NO")
else:
    print("YES")
