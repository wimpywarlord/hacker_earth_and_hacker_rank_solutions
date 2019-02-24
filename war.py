t=int(input())
for i in range(0,t):
     x=int(input())
     y=input()
     z=input()
     a=y.split()
     b=z.split()
     print(a)
     print(b)
     suma=0
     sumb=0
     for k in range(0,x):
         suma=suma+a[k]
         sumb=sumb+b[k]
         #if int (a[k])>int(b[k]):
           #  countera+=1
           #  print(countera,"$")
        # elif int(a[k])<int(b[k]):
            # counterb+=1
            # print(counterb,"*")
     if suma==sumb:
         print("Tie")
     elif suma>sumb:
         print("Bob")
     elif suma<sumb:
         print("Alice")
