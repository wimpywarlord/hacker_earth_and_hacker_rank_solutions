n,k=map(int,input().split())
obs=[]
queen=list(map(int,input().split()))
queen[0]=n-queen[0]+1
queen[1]=queen[1]-1+1
#print(queen)
for i in range(0,k):
    z=list(map(int,input().split()))
    obs.append(z)
#print(obs)
mat=[]
for i in range(0,n):
    mat.append([])
    for j in range(0,n):
        mat[i].append(1)
mat.insert(0,[])
mat.insert(n+1,[])

for i in range(0,n+2):
    mat[0].append(0)
    mat[-1].append(0)
for i in range(1,n+1):
    mat[i].append(0)
    mat[i].insert(0,0)
#print(mat)
for i in range(0,k):
    obs[i][0]=n-obs[i][0]+1
    obs[i][1]=obs[i][1]-1+1
#print(obs)
mat[queen[0]][queen[1]]=5
for i in range(0,k):
    mat[obs[i][0]][obs[i][1]]=3

'''for i in range(0,n+2):
    for j in range(0,n+2):
        print(mat[i][j],end=' ')
    print()'''
ans=0
flag1=0
flag2=0
flag3=0
flag4=0
flag5=0
flag6=0
flag7=0
flag8=0
ctr=0
while flag1==0 or flag2==0 or flag3==0 or flag4==0 or flag5==0 or flag6==0 or flag7==0 or flag8==0:
    ctr+=1
    if flag1==0:
        if mat[queen[0]+ctr][queen[1]]==1 and flag1==0:
            mat[queen[0]+ctr][queen[1]]=9
            ans+=1
        else:
            flag1=1
    if flag2==0:
        if mat[queen[0]-ctr][queen[1]]==1 and flag2==0:
            mat[queen[0]-ctr][queen[1]]=9
            ans+=1
        else:
            flag2=1
    #print(mat[queen[0]][queen[1]+ctr])
    if flag3==0:
        if mat[queen[0]][queen[1]+ctr]==1:
            mat[queen[0]][queen[1]+ctr]=9
            ans+=1
        else:
            flag3=1
    if flag4==0:
        if mat[queen[0]][queen[1]-ctr]==1 and flag4==0:
            mat[queen[0]][queen[1]-ctr]=9
            ans+=1
        else:
            flag4=1
    if flag5==0:
        if mat[queen[0]-ctr][queen[1]-ctr]==1 and flag5==0:
            mat[queen[0]-ctr][queen[1]-ctr]=9
            ans+=1
        else:
            flag5=1
    if flag6==0:
        if mat[queen[0]-ctr][queen[1]+ctr]==1 and flag6==0:
            mat[queen[0]-ctr][queen[1]+ctr]=9
            ans+=1
        else:
            flag6=1
    if flag7==0:
        if mat[queen[0]+ctr][queen[1]-ctr]==1 and flag7==0:
            mat[queen[0]+ctr][queen[1]-ctr]=9
            ans+=1
        else:
            flag7=1
    if flag8==0:
        if mat[queen[0]+ctr][queen[1]+ctr]==1 and flag8==0:
            mat[queen[0]+ctr][queen[1]+ctr]=9
            ans+=1
        else:
            flag8=1
    
#print(ctr)
'''for i in range(0,n+2):
    for j in range(0,n+2):
        print(mat[i][j],end=' ')
    print()'''
print(ans)
