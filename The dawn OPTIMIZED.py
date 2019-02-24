n=int(input())
factors=[]
for i in range(2,n):
    for j in range(i,n):
        while n%j==0:
            n=n//j
            print(n)
            factors.append(j)
        
print(factors)
summ=0
for j in range(0,len(factors)):
    summ=summ+factors[j]
print(summ  + 1)
