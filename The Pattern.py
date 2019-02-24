t=int(input())
for i in range(0,t):
    z=input()
    n,m=z.split()
    n=int(n)
    m=int(m)
    mat=[]
    for j in range(0,n):
        x=input()
        mat.append([])
        for k in range(0,len(x)):
            mat[j].append(x[k])
    print(mat)
    newmat=[]
    for j in range(0,n-1):
        newmat.append([])
        for k in range(0,m):
            newmat[j].append('#')
    for j in range(0,len(mat)-1):
        for k in range(0,len(mat[j])):
            if j==0 and j!=len(mat)-1:
                if mat[j][k]=='*' and mat[j+1][k]=='.':
                    newmat[j][k]='.'
                elif mat[j][k]=='.' and mat[j+1][k]=='.':
                    newmat[j][k]='.'
                elif mat[j][k]=='.' and mat[j+1][k]=='*':
                    newmat[j][k]='*'
                elif mat[j][k]=='*' and mat[j+1][k]=='*':
                    newmat[j][k]='*'
    print(newmat)
