n=int(input())
s=input()
ctr=0
ptr=0
for i in range(0,len(s)):
    if ctr==0:
        flag=s[i]
        print(i,flag,"%")
    if s[i]=='U':
        ctr+=1
    if s[i]=='D':
        ctr-=1
    if ctr==0 and flag=='D':
        ptr+=1
print(ptr)
