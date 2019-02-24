y=input()
p,s,t,h,x=y.split()
p=int(p)
s=int(s)
t=int(t)
h=int(h)
x=int(x)
pay=0
if x>s:
    print(0)
else:

    while x>0:
        print(x)
        if s>t:
            pay+=p
            x-=1
            s-=1
        elif s<=t:
            pay+=h
            x-=1
            s-=1

print(pay)
    
