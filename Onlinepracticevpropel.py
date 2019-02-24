s=input()
l=[]
for i in range(0,len(s)):
    l.append(s[i])
print(l)
if l[len(l)-1]='M' and l[len(l)-2]=='A':
    print("%")
else:
    print("^")
