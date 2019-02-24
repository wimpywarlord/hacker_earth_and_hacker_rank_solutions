t=int(input())
for i in range(0,t):
    au=input()
    a,u=au.split()
    print(int(a))
    print(int(u))
    path=input()
    b=path.split()
    for j in range(0,int(u)):
        b[j]=int(b[j])
    print(b)
    counter=0
    for k in b:
        counter+=1
        if k==0:
            a=int(a)-1
            print(int(a))
        elif k==1 :
            a=int(a)+2
            print(int(a))
        if a==0:
            break
    if int(a)==0 and counter == int(u):
        print("Yes")
        print("0")
    elif int(a)<=0 and counter !=int(u):
        print("No")
        print(counter)
    else:
        print("Yes")
        print(int(a))
            
