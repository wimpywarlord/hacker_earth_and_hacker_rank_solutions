s=input()
d={}
for i in range(0,len(s)):
    d[s[i]]=0
for i in range(0,len(s)):
    d[s[i]]+=1
dk=list(d.keys())
#print(dk)
l=[]
for i in range(0,len(dk)):
    l.append([])
    for j in range(0,len(s)):
        if s[j]!=dk[i]:
            l[i].append(s[j])
#print(l)
l.sort()
ans=''
for i in range(0,len(l[0])):
    ans+=l[0][i]
print(ans)
