ss=input()
s=[]
for i in range(0,len(ss)):
    s.append(ss[i])
ans=''
for i in range(0,len(s)):
    ans+=s[i]
for i in range(0,len(s)):
    x=len(ans)
    #print(x)
    for j in range(0,x):
        if j!=x-1:
            if s[j]==s[j+1]:
                s[j]=0
                s[j+1]=0
    ans=''
    for j in range(0,x):
        if s[j]!=0:
            ans+=s[j]
    s=[]        
    for j in range(0,len(ans)):
        s.append(ans[j])
    
if not s:
    print("Empty String")
else:
    print(ans)
        
