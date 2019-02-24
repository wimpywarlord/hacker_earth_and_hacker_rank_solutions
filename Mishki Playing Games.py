xx=input()
n,q=xx.split()
n=int(n)
q=int(q)
yy=input()
l=yy.split()
rrr=yy.split()

for i in range(0,len(rrr)):
    rrr[i]=int(rrr[i])
for i in range(0,len(l)):
    l[i]=int(l[i])
print(l)
print(rrr)
for i in range(0,q):
    ctr=0
    print(ctr)
    for v in range(0,len(l)):
        l[v]=rrr[v]
    print(l)
    zz=input()
    left,right=zz.split()
    left=int(left)-1
    print(left)
    right=int(right)
    print(right)
    print(l)
    for i in range(left,right):
            print(l[i])
            while l[i]>0:
                ctr+=1
                print(l[i],"$")
                l[i]=l[i]//2
                print(l[i],"%")

    print(ctr)
    if ctr%2==0:
        print("Hacker")
    else:
        print("Mishki")
    

