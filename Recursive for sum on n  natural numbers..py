t=0
def func(n):
    if n>=0:
        global t
        t+=n
        n-=1
        func(n)
        return t
    
n=int(input())
x=func(n)
print(t)
print(x)


