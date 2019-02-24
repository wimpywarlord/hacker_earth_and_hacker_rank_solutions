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
sss=0
flag=0
while odays%7!=0 and rr!=tt :    
    while sss==0 :
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
        if odays%7==0:
            flag=1
        else:
            flag=0
            
        if flag==1:
            if (n+1)%400==0 or (n+1)%100!=0 and (n+1)%4==0:
                rr=2
            else:
                rr=1
            print(rr)
        else:
            rr=0
        if rr==tt :
            sss=1
print()            
print(n+1)
