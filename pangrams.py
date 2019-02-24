s=input()
s=s.lower()
d={}
for i in range(0,len(s)):
    if s[i]!=' ':
        d[s[i]]=0
for i in range(0,len(s)):
    if s[i]!=' ':
        d[s[i]]+=1
#print(d)
#print(len(d))
if len(d)==26:
    print("pangram")
else:
    print("not pangram")
