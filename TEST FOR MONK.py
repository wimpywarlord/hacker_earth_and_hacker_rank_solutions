n=int(input())
a=input()
aa=[]
for i in a:
    aa.append(i)
aa.sort()
b=input()
bb=[]
for i in b:
    bb.append(i)
bb.sort()
print(aa)
print(bb)
if aa==bb:
    print("YES")
else:
    print("NO")
