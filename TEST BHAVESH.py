s=input()
x=[]
for i in range(0,len(s)):
    x.append(s[i])
print(x)
for i in range(len(s)):
    for j in range(len(s),i,-1):
        for k in range(j):
            print(x[k],end=' ')
        print()
        continue
        
