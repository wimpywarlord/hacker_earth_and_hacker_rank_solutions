t=int(input())
for i in range(0,t):
    n=int(input())
    z=input()
    a=z.split()
    for j in range(0,len(a)):
        a[j]=int(a[j])
    #print(a)
    v=[]
    
    for j in range(0,len(a)):
        if a[j]>=10:
            while a[j]>0:
                g=a[j]%10
                v.append(g)
                a[j]=a[j]//10
        else:
            v.append(a[j])
    v.sort(reverse=True)
    for j in range(0,len(v)):
        print(v[j],end='')
    print()

