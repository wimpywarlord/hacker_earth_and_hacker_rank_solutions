t=int(input())
for i in range(0,t):
    z=list(input())
    x=sorted(z)
    flag=0
    for j in range(0,len(x)):
        if j!=len(x)-1:
            if int(x[j+1])-int(x[j])>1 or int(x[j+1])-int(x[j])==0:
                flag=1
    if flag==1:
        print("NO")
    else:
        print("YES")
    
