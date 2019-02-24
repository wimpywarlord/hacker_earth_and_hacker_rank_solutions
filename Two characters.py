n=int(input())
s=list(input())
d={}
for i in range(0,len(s)):
    d[s[i]]=0
for i in range(0,len(s)):
    d[s[i]]+=1
#print(d)
use=[]
ctr=0
keys=list(d.keys())
for i in range(0,len(keys)):
    for j in range(i,len(keys)):
        for k in range(j+1,len(keys)):
            use.append([])
            use[ctr].append(keys[j])
            use[ctr].append(keys[k])
            ctr+=1
        break
#print(use)
final=[]
for i in range(0,len(use)):
    temp=''
    for k in range(0,len(s)):
        if s[k]==use[i][1] or s[k]==use[i][0]:
            temp+=s[k]
    #print(temp)
    final.append(temp)
#print(final)
ans=[]
for i in range(0,len(final)):
    flag=0
    for  j in range(0,len(final[i])):
        if j!=len(final[i])-1:
            if final[i][j]==final[i][j+1]:
                flag=1
    if flag==0:
        ans.append(len(final[i]))
if not ans:
    print(0)
else :
    print(max(ans))
    
