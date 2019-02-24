n=int(input())
aa=input()
a=aa.split()
bb=input()
b=bb.split()
for i in range(0,len(a)):
    a[i]=int(a[i])
for i in range(0,len(b)):
    b[i]=int(b[i])
#print(a)
#print(b)
v=[]
for i in range(0,len(a)):
    v.append([])
    for j in range(0,len(a)):
        if a[i]==a[j]:
            v[i].append(b[j])
            v[i].append(b[i])
ans=[]
for i in range(0,len(v)):
    for j in range(0,len(v[i])):
        ans.append(max(v[i]))
        break
for i  in range(0,len(ans)):
    print(ans[i],end=' ')
