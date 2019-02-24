t=int(input())
for i in range(0,t):
    x=int(input())
    l=[]
    for j in range(1,x+1):
        l.append(j)
    #print(l)
    ctr=0
    y=len(l)
    while y!=1:
        del l[ctr]
        l.append(l[0])
        del l[ctr]
        y=len(l)
    print(l[0])      
