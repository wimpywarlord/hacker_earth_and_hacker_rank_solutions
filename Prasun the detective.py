s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
#print(s1)
#print(s2)
from collections import defaultdict
d1=defaultdict(int)
d2=defaultdict(int)
for i in range(0,len(s1)):
    if s1[i]!=' ':
        d1[s1[i]]+=1
for i in range(0,len(s2)):
    if s2[i]!=' ':
        d2[s2[i]]+=1
#print(d1)
flag=0
d1key=list(d1.keys())
d2key=list(d2.keys())
for i in range(0,len(d2key)):
    if d2key[i] in d1key :
        if d2[d2key[i]]>d1[d2key[i]]:
            flag=1
            #print("*")
    if d2key[i] not in d1key:
        flag=1
        #print(d2key[i])
        #print("@")
if flag==0:
    print("YES")
else:
    print("NO")
#print(d2)
