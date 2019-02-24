n=int(input())
z=input()
a=z.split()
for i in range(0,len(a)):
    a[i]=int(a[i])
#print(a)
for i in range(0,len(a)):
    pos=i
    for j in range(0,len(a)):
        if a[j]==pos+1:
            print(a[a[j]-1])
