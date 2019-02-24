l=int(input())
a=input()
b=a.split()
for i in range(0,l):
    b[i]=int(b[i])
print(b)

for i in range(0,l + 1):
     if i + b[i]>= l:
         print(i+1)
         break
