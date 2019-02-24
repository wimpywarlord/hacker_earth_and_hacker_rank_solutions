n=int(input())
z=input()
l=z.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
#print(l)
ans=[]
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]==l[j] and j!=i:
            ans.append(abs(j-i))
#print(ans)
if not ans:
    print(-1)
else:
    print(min(ans))
