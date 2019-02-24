n=int(input())
ss=input()
s=[]
for i in range(0,len(ss)):
    s.append(ss[i])
#print(s)
k=int(input())
k=k%26
for i in range(0,len(s)):
    if 65<=ord(s[i])<=90:
        if ord(s[i])+k<=90:
            s[i]=chr(ord(s[i])+k)
        else:
            s[i]=chr(64+(ord(s[i])+k)%90)
    if 97<=ord(s[i])<=122:
        if ord(s[i])+k<=122:
            s[i]=chr(ord(s[i])+k)
        else:
            s[i]=chr(96+(ord(s[i])+k)%122)
ans=''
for i in range(0,len(s)):
    ans+=s[i]
print(ans)
        
