t=int(input())
for i in range(0,t):
    z=input()
    n,k=z.split()
    n=int(n)
    k=int(k)
    y=input()
    att=y.split()
    for j in range(0,len(att)):
        att[j]=int(att[j])
    print(att)
    ctr=0
    for j in range(0,len(att)):
        if att[j]<=0:
            ctr+=1
    if ctr>=k:
        print("NO")
    else:
        print("YES")
            
