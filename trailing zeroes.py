n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
count=0
num=[]
while fact>0:
   y=fact%10 
   num.append(y)
   fact//=10
print(num)
for i in num:
    if i!=0:
        break
    count+=1
print(count)
