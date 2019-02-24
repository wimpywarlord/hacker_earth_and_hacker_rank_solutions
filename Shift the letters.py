s=list(input())
#print(s)
k=int(input())
diff=[]
for i in range(0,len(s)):
    if i!=len(s)-1:
        temp=abs(ord(s[i])-ord(s[i+1]))
        diff.append(temp)
print(diff)
ctr=0
index=[]
for  i in range(0,k):
    z=max(diff)
    for i in range(0,len(s)):
        if diff[i]==z:
            diff[i]=-1
            index.append(i)
            break
print(diff)
#print(index)
ptr=0
for i in range(0,len(index)):
    s.insert(index[i]+ptr+1,'-')
    ptr+=1
use=[]
usectr=0
s.insert(0,'-')
print(s)
for i in range(0,len(s)):
    if s[i]=='-':
        use.append([])
        for j in range(i+1,len(s)):
            if s[j]=='-':
                break
            else:
                use[usectr].append(s[j])
        usectr+=1
print(use)
minuse=[]
ctrminuse=0
for i in range(0,len(use)):
    minuse.append([])
    for j in range(0,len(use[i])):
        paisa=0
        for g in range(0,len(use[i])):
            if ord(use[i][j])<ord(use[i][g]) and j!=g:
                paisa +=122 - ord(use[i][g]) + ord(use[i][j])-96
            else:
                paisa+=abs(ord(use[i][j])-ord(use[i][g]))
        minuse[ctrminuse].append(paisa)
    ctrminuse+=1
print(minuse)
minuseindex=[]
ans=0
for i in range(0,len(minuse)):
    zz=min(minuse[i])
    ans+=zz
print(ans)
