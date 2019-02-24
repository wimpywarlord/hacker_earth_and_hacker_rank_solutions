n=int(input())
s=input()
l=s.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
print(l)
maxx=l[0]
minn=l[0]
ctr1=0
ctr2=0
for i in range(1,len(l)):
    if maxx<l[i]:
        ctr1+=1
        print("^")
        maxx=l[i]
    if minn>l[i]:
        ctr2+=1
        print("#")
        minn=l[i]
print(ctr1,ctr2)
