y=input()
x1,v1,x2,v2=y.split()
x1=int(x1)
v1=int(v1)
x2=int(x2)
v2=int(v2)
if x2>=x1 and v2>v1:
    print("NO")
elif x1>=x2 and v1>v2:
    print("NO")
else:
    p=x1+v1
    q=x2+v2
    if p==q:
        print("YES")
    else:
        flag=0
        for i in range(1,1000000):
            p=p+v1
            q=q+v2
            if p==q:
                print("YES")
                flag=1
                break
        if flag==0:
            print("NO")
            
        
