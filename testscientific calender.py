n=int(input())
odays=0
tt=0
if n%100==0:
    if n%400==0:
        odays=2
        tt=2
    elif n%400!=0:
        odays=1
        tt=1

if n%100!=0:
    if n%4==0:
        odays=2
        tt=2
    elif n%4!=0:
        odays=1
        tt=1
print(odays)
print()
rr=0
while True :
    n+=1
    if n%400==0 or n%100!=0 and n%4==0:
        rr=2
    else:
        rr=1
    print(rr)
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
    if odays%7==0 and tt==rr:
        break
print()            
print(n+1)
