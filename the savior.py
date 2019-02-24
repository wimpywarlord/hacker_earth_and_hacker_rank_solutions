t=int(input())
for i in range(0,t):
    n=int(input())
    x=input()
    a=x.split()
    print(a)
    for i in range(0,n):
        a[i]=int(a[i])
    b=[]
    counter=0
    result=[]
    for i in range(0,n):
        for j in range(0,n):
          if i!=j: 
            if (a[i] + a[j])%2==0 and a[i]!=a[j]:
                    b.append([])
                    b[counter].append(a[i])
                    b[counter].append(a[j])
                    counter+=1
                
    print(b)
    for k in b:        
        g=k[::-1]
        if k not in result and g not in result:
            result.append(k)
    print(result)
    print(len(result))

