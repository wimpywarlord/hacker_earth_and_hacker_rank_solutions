ss=input()
s=[]
for i in range(0,len(ss)):
    s.append(ss[i])
print(s)
if s[len(s)-2]=='A':
    if s[0]=='1' and s[1]=='2':
        s[0]='0'
        s[1]='0'
    for i in range(0,len(s)-2):
        print(s[i],end='')
else:
    if s[0]=='1' and s[1]=='2':
        pass
    else:
        x=int(s[0])
        #print(x)
        y=int(s[1])
        #print(y)
        fit=x*10+y+12
        #print(fit)
        p=fit%10
        q=fit//10
        #print(p)
        #print(q)
        s[0]=q
        s[1]=p
    for i in range(0,len(s)-2):
        print(s[i],end='')
    
