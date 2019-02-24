n=int(input())
flag=1
summ=0
while flag==1:
    while n>0:
       g=n%10
       summ=summ+g
       n=n//10
    if summ<10:
       print(summ)
       flag=0
    else :
       n=summ
