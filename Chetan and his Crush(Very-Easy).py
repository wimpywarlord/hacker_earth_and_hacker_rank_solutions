n=int(input())
x=input()
l=x.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
print(l)
for i in range(0,len(l)):
    s=i+1
    s=s+l[i]
    if s>len(l):
        print(i+1)
        break
        
