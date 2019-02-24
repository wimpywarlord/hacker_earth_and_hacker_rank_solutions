s=input()
n=int(input())
'''ctr=0
flag=0
for i in range(0,len(s)):
    if s[i]!='a':
        flag=1
if flag==1:
    for i in range(0,n):
        if i>=len(s):
            i=i%len(s)
            if s[i]=='a':
                ctr+=1
        else:
            if s[i]=='a':
                ctr+=1
    print(ctr)
else:
    print(n)'''
ctr=0
for i in range(0,len(s)):
    if s[i]=='a':
        ctr+=1
#print(ctr)
ans=ctr*(n//len(s))
g=n%len(s)
for i in range(0,g):
    if s[i]=='a':
        ans+=1
print(ans)
