n=input("ENTRE THE NUMBER :")
summ=0 
for i in n:
    x=ord(i)
    if (x-48) % 2==0 :
        summ=summ*10 + x- 48
print(summ)
