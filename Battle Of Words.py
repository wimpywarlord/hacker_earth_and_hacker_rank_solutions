t=int(input())
for q in range(0,t):
    x=input()
    l1=[]
    l11=list(x.split())
    y=input()
    for i in range(0,len(l11)):
        l1.append([])
        for j in range(0,len(l11[i])):
            l1[i].append(l11[i][j])
    print(l1)
    l2=[]
    l22=list(y.split())
    for i in range(0,len(l22)):
        l2.append([])
        for j in range(0,len(l22[i])):
            l2[i].append(l22[i][j])
    print(l2)
    for i in range(0,len(l1)):
        for j in range(0,len(l1[i])):
            for k in range(0,len(l2)):
                for n in range(0,len(l2[k])):
                    if l2[k][n]==l1[i][j]:
                        l2[k][n]=0
                        l1[i][j]=0
    print(l1)
    print(l2)
    flag1=0
    for i in range(0,len(l1)):
        for j in range(0,len(l1[i])):
            if l1[i][j]!=0:
                flag1=1
    flag2=0
    for i in range(0,len(l2)):
        for j in range(0,len(l2[i])):
            if l2[i][j]!=0:
                flag2=1
    if flag1==1 and flag2==0:
        print('You win some.')
    elif flag1==0 and flag2==1:
        print("You lose some.")
    elif flag1==1 and flag2==1:
        print("You draw some.")
                
            
    
    
