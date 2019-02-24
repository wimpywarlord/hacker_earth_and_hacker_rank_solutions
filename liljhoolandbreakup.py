a=input()
b=[]
for i in range(0,len(a)):
        b.append(a[i])
flag=0
for i in range(0,len(b)):
    if a[i]=='l':
        for j in range(i,len(b)):
            if a[j]=='o':
                for k in range(j,len(b)):
                    if a[k]=='v':
                        for l in range(k,len(b)):
                            if a[l]=='e':
                                flag=1
if flag==0:
    print("Let us breakup!")
else:
    print("I love you, too!")

        

