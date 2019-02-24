l=[0,0,0,1,0,1,1,0,0,0,0,1]
l1=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[j]!=0 and j>=i:
            l1[i]=abs((j+1)-(i+1))
            break
print(l1)
