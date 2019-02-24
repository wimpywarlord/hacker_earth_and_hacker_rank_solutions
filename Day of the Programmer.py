n=int(input())
if n>1918:
    if n%400==0 or (n%4==0 and n%100!=0):
        print('12.09.',end='')
        print(n)
    else:
        print('13.09.',end='')
        print(n)
if n<1918:
    if n %4==0:
        print('12.09.',end='')
        print(n)
    else:
        print('13.09.',end='')
        print(n)
if n==1918:
    print('27.09.1918')
