t=int(input())
for i in range(0,t):
    tic=[]
    for j in range(0,4):
        x=input()
        tic.append([])
        tic[j].append(x[0])
        tic[j].append(x[1])
        tic[j].append(x[2])
        tic[j].append(x[3])
    print(tic)
    flag=0
    for j in range(0,len(tic)):
        for k in range(0,len(tic[j])):
            if k==0 or k==1:
                if tic[j][k]=='x' and tic[j][k+1]=='x' and tic[j][k+2]=='.':
                    flag=1
                if tic[j][k]=='.' and tic[j][k+1]=='x' and tic[j][k+2]=='x':
                    flag=1
                if tic[j][k]=='x' and tic[j][k+1]=='.' and tic[j][k+2]=='x':
                    flag=1
    for k in range(0,len(tic[j])):
        for j in range(0,len(tic)):
            if j==0 or j==1:
                if tic[j][k]=='x' and tic[j+1][k]=='x' and tic[j+2][k]=='.':
                    flag=1
                if tic[j][k]=='.' and tic[j+1][k]=='x' and tic[j+2][k]=='x':
                    flag=1
                if tic[j][k]=='x' and tic[j+1][k]=='.' and tic[j+2][k]=='x':
                    flag=1
                    
    if tic[0][0]=='x' and tic[1][1]=='x' and tic[2][2]=='.':
        flag=1
    if tic[0][0]=='x' and tic[1][1]=='.' and tic[2][2]=='x':
        flag=1
    if tic[0][0]=='.' and tic[1][1]=='x' and tic[2][2]=='x':
        flag=1


    if tic[0][1]=='x' and tic[1][2]=='x' and tic[2][3]=='.':
        flag=1
    if tic[0][1]=='x' and tic[1][2]=='.' and tic[2][3]=='x':
        flag=1
    if tic[0][1]=='.' and tic[1][2]=='x' and tic[2][3]=='x':
        flag=1


    if tic[0][2]=='x' and tic[1][1]=='x' and tic[2][0]=='.':
        flag=1
    if tic[0][2]=='x' and tic[1][1]=='.' and tic[2][0]=='x':
        flag=1
    if tic[0][2]=='.' and tic[1][1]=='x' and tic[2][0]=='x':
        flag=1


    if tic[0][3]=='x' and tic[1][2]=='x' and tic[2][1]=='.':
        flag=1
    if tic[0][3]=='x' and tic[1][2]=='.' and tic[2][1]=='x':
        flag=1
    if tic[0][3]=='.' and tic[1][2]=='x' and tic[2][1]=='x':
        flag=1


    if tic[3][0]=='x' and tic[2][1]=='x' and tic[1][2]=='.':
        flag=1
    if tic[3][0]=='x' and tic[2][1]=='.' and tic[1][2]=='x':
        flag=1
    if tic[3][0]=='.' and tic[2][1]=='x' and tic[1][2]=='x':
        flag=1

    if tic[3][1]=='x' and tic[2][2]=='x' and tic[1][3]=='.':
        flag=1
    if tic[3][1]=='x' and tic[2][2]=='.' and tic[1][3]=='x':
        flag=1
    if tic[3][1]=='.' and tic[2][2]=='x' and tic[1][3]=='x':
        flag=1


    if tic[3][2]=='x' and tic[2][1]=='x' and tic[1][0]=='.':
        flag=1
    if tic[3][2]=='x' and tic[2][1]=='.' and tic[1][0]=='x':
        flag=1
    if tic[3][2]=='.' and tic[2][1]=='x' and tic[1][0]=='x':
        flag=1

    if tic[3][3]=='x' and tic[2][2]=='x' and tic[1][1]=='.':
        flag=1
    if tic[3][3]=='x' and tic[2][2]=='.' and tic[1][1]=='x':
        flag=1
    if tic[3][3]=='.' and tic[2][2]=='x' and tic[1][1]=='x':
        flag=1


    
    if flag==1:
        print("YES")
    else:
        print("NO")
