def f(d):
    fact=1
    for i in range(1,d+1):
        
        fact*=i
    return fact
x=int(input())
a=f(x)
print(a)
