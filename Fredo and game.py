t=int(input())
for i in range(0,t):
    am=int(input())
    un=int(input())
    a=[]
    for j in range(0,un):
       x=int(input())
       a.append(x)
    print(a)
    print(am)
    print(un)
    for k in range(0,un):
       if  int(a[i]) == '0':
           am=am-1
           print(am)
       elif  int(a[i]) == '1':
           am=am + 2
           print(am)
    if am<0:
        print("No")
        print(am)
    else :
        print("Yes")
        print(am)

