n=int(input())
aa=input()
a=[]
b=[]
for i in range(0,n):
    a.append(aa[i])
print(a)
bb=input()
for i in range(0,n):
    b.append(bb[i])
print(b)
count=0
tt=0
for i in range(0,n):
    for j in range(0,n):
        if a[i]==b[j]:
            b[j]=tt
            count+=1
            print(b)
        tt+=1
if count!=n:
    print("NO")
else:
    print("YES")
