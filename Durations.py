n=int(input())
for i in range(0,n):
    x=input()
    l=x.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    print(l)
    sh=l[0]
    sm=l[1]
    eh=l[2]
    em=l[3]
    ansh=eh-sh-1
    ansm=60-sm + em
    if ansm>=60:
        ansm=ansm%60
        ansh+=1
    print(ansh,ansm)
