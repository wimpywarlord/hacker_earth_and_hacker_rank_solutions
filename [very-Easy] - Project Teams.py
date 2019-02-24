n=int(input())
ctr=0
while n>3:
    if n-3<3:
        break
    n=n-3
    ctr+=1
#print(n)
print(ctr+1)
