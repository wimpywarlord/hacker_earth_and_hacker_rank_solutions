x=input()
n,k=x.split()
n=int(n)
k=int(k)
#print(n)
#print(k)
y=input()
l=y.split()
charge=int(input())
#print(charge)
for i in range(0,len(l)):
    l[i]=int(l[i])
#print(l)
summ=0
for i in range(0,len(l)):
    if i==k:
        pass
    else:
        summ+=l[i]
#print(summ)
if charge==abs(charge-summ):
    print("Bon Appetit")
else:
    print(abs(charge-summ//2))
