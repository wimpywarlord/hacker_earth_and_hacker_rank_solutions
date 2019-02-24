z=input()
dr,mr,yr=z.split()
d1=int(dr)
m1=int(mr)
y1=int(yr)
y=input()
d2,m2,y2=y.split()
d2=int(d2)
m2=int(m2)
y2=int(y2)
ans=0
if y1-y2>0:
    ans=10000
elif m1-m2>0 and y1==y2 :
    ans=500*abs(m2-m1)
elif d1-d2>0 and y1==y2 and m1==m2:
    ans=15*abs(d2-d1)
print(ans)
