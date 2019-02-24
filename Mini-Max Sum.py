x=input()
l=x.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
ans=[]
for i in range(len(l)):
    summ=0
    for j in range(0,len(l)):
        if l[i]==l[j] and i==j:
            pass
        else:
            summ+=l[j]
    ans.append(summ)

print(min(ans),end=' ')
print(max(ans))
