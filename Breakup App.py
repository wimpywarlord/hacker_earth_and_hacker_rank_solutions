n=int(input())
use=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
from collections import defaultdict
d=defaultdict()
for i in range(0,n):
    s=list(input().split())
    #print(s)
    dkey=list(d.keys())
    #print(dkey)
    if s[0]=='G:':
        #print("@")
        for j in range(len(s)):
            if s[j] in use and int(s[j]) not in dkey:
                #print(s[j],"%")
                d[int(s[j])]=2
            elif s[j] in use and int(s[j]) in dkey:
                #print(s[j],"^")
                d[int(s[j])]+=2
    elif s[0]=='M:':
        #print("!")
        for j in range(len(s)):
            if s[j] in use and int(s[j]) not in dkey:
                #print(s[j],"&")
                d[int(s[j])]=1
            elif s[j] in use and int(s[j]) in dkey :
                #print(s[j],"*")
                d[int(s[j])]+=1
flag=0
dval=list(d.values())
#print(d)
for i in range(0,len(dval)):
    for j in range(0,len(dval)):
        if dkey[i]==dkey[j] and i!=j:
            flag=1
            print("No Date")
if not dval:
    print("No Date")
else:
    store=max(dval)
    for i in range(0,len(dkey)):
        if d[dkey[i]]==store:
            if dkey[i]==19 or dkey[i]==20:
                print("Date")
            else:
                print("No Date")

        
            

