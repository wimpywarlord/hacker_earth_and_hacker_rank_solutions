n=int(input())
ctr=0
for i in range(0,n):
    x=input()
    w,h=x.split()
    w=int(w)
    h=int(h)
    q=w/h
    a=h/w
    #print(q)
    if 1.6000000<=q<=1.7000000 or 1.6000000<=a<=1.7000000:
        ctr+=1
print(ctr)
