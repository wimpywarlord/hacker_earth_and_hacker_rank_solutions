n=int(input())
a=[]
for j in range(0,n):
    counter=0
    nop=int(input())
    x=input()
    b=x.split()
    
    for k in range(0,nop):
      a.append(int(b[k]))
    print(a)
    for k in range(0,nop):
      if a[k]%2==0:
        while a[k]%2==0:
            a[k]=a[k]/2
            counter+=1
      else :
        continue
    if counter%2==0 and counter!=0 :
      print("Alan")
    else:
      print("Charlie")
    while nop>0:
        a.pop()
        nop-=1
    print(a)
