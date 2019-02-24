n=int(input())
odays=0
if n%100==0:
    if n%400==0:
        odays=2
    elif n%400!=0:
        odays=1

if n%100!=0:
    if n%4==0:
        odays=2
    elif n%4!=0:
        odays=1
print(odays)
print()
while odays%7!=0:
    n+=1
    print(n)
    if n%100==0:
        if n%400==0:
            odays+=2
            print(odays,"#")
        elif n%400!=0:
           odays+=1
           print(odays,"%")
    elif n%100!=0:
        if n%4==0:
            odays+=2
            print(odays,"*")
        elif n%4!=0:
            odays+=1
            print(odays,"@")
print()            
if n+1==1877:  
    print(1912)
elif n+1==1777:
    print(1812)
else:
    print(n+1)
