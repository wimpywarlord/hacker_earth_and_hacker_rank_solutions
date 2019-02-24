s1=input()
s2=input()
y=[]
for i in range(0,len(s2)):
    y.append(s2[i])
print(y)
x=[]
ctr=0
for i in range(0,len(s1)):
    for j in range(i,len(s1)):
        x.append([])
        for k in range(j,len(s1)):
            print(s1[k],end=' ')
            x[ctr].append(s1[k])
        ctr+=1    
        print()
print(x)
if y not in x:
    print("False")
else:
    print("True")
