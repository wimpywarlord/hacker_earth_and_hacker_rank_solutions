n=int(input())
mat=[]
for i in range(0,n):
    z=input()
    mat.append([])
    for j in range(0,len(z)):
        mat[i].append(z[j])
for i in range(1,len(mat)-1):
    for j in range(1,len(mat[i])-1):
        if mat[i][j]>mat[i+1][j] and mat[i][j]>mat[i-1][j] and mat[i][j]>mat[i][j+1] and mat[i][j]>mat[i][j-1] :
            mat[i][j]='X'
for i  in range(0,len(mat)):
    for j in range(0,len(mat[i])):
        print(mat[i][j],end='')
    print()
#print(mat)
    
