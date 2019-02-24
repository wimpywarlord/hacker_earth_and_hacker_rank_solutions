n=int(input())
s=[]
for i in range(0,n):
    x=input()
    s.append(x)
#print(s)
log=[]
ctr=0
for i in range(0,len(s)):
    ctr=0
    check=[]
    flag=0
    for j in range(0,len(s[i])):
        if s[i][j]=='C':
            ctr+=1
        else:
            check.append(ctr)
            flag=1
            ctr=0
    print(check)
    if flag==1:
        print(log)
        log.append(max(check))
    else:
        log.append(ctr)
print(max(log),end=' ')
m=[]
flag2=0
ctr2=0
for i in range(0,len(s)):
    for j in range(0,len(s[i])):
        if s[i][j]=='C':
            ctr2+=1
        else:
            m.append(ctr2)
            flag2=1
            ctr2=0    
if flag2==1:
    print(max(m))
else:
    print(ctr2)

        
