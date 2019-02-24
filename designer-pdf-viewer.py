z=input()
l=z.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
print(l)
s=input()
v=[]
for i in range(0,len(s)):
    p=ord(s[i])-97
    v.append(l[p])
print(v)
print(max(v)*len(s))    
