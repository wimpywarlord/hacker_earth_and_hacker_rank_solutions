s=input()
username=""
ctr=0
for i in range(0,len(s)):
    if s[i]=="=":
        j=i+1
        while s[j]!="&":
            username+=s[j]
            j+=1
        ctr=i
        break
print("username:",username)
pwd=""
for i in range(0,len(s)):
    if s[i]=="=" and i>ctr:
        j=i+1
        while s[j]!="&":
            pwd+=s[j]
            j+=1
        ctr=i
        break
print("pwd:",pwd)
profile=""
for i in range(0,len(s)):
    if s[i]=="=" and i>ctr:
        j=i+1
        while s[j]!="&":
            profile+=s[j]
            j+=1
        ctr=i
        break
print("profile:",profile)
role=""
for i in range(0,len(s)):
    if s[i]=="=" and i>ctr:
        j=i+1
        while s[j]!="&":
            role+=s[j]
            j+=1
        ctr=i
        break
print("role:",role)
key=""
for i in range(0,len(s)):
    if s[i]=="=" and i>ctr:
        j=i+1
        while j!=len(s):
            key+=s[j]
            j+=1
        ctr=i
        break
print("key:",key)
