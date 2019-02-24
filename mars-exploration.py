s=input()
l=[]
ctr=0
for i in range(0,len(s),3):
    l.append([])
    l[ctr].append(s[i])
    l[ctr].append(s[i+1])
    l[ctr].append(s[i+2])
    ctr+=1
#print(l)
ans=0
for i in range(0,len(l)):
    if l[i][0]!='S':
        ans+=1
    if l[i][1]!='O':
        ans+=1
    if l[i][2]!='S':
        ans+=1
print(ans)

