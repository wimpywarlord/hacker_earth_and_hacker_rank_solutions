t=int(input())
for  i in range(0,t):
    n=int(input())
    v=[]
    for j in range(0,n):
        z=input()
        v.append([])
        for k in range(0,len(z)):
            v[j].append(z[k])
    #print(v)
    flagh=0
    flagv=0
    ctr=0
    for j in range(0,len(v)//2):
        for k in range(0,n):
            if  v[j][k]!=v[len(v)-1-j][k]:
                #print(v[j][k],v[len(v)-1-j][k])
                flagh=1

    for j in range(0,len(v)):
        for k in range(0,len(v[j])):
            if v[k][j]!=v[k][len(v)-1-j]:
                flagv=1
    if flagh==0 and flagv==0:
        print("BOTH")
    elif flagh==0 and flagv==1:
        print("HORIZONTAL")
    elif flagv==0 and flagh==1:
        print("VERTICAL")
    elif flagv==1 and flagh==1:
        print("NO")
                
                
