t=int(input())
for i in range(0,t):
    x=input()
    b,w=x.split()
    b=int(b)
    w=int(w)
    y=input()
    bc,wc,z=y.split()
    bc=int(bc)
    wc=int(wc)
    z=int(z)
    if z>bc and z>wc:
        print(bc*b+wc*w)
    elif bc>(wc+z):
        print(wc*w+b*(z+wc))
    elif  wc>(bc+z):
        print((bc+z)*w+bc*(b))
    else:
        print(bc*b+wc*w)
