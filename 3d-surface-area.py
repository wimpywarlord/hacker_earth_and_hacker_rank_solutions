r,c=map(int,input().split())
mat=[]
for i in range(0,r):
    s=list(map(int,input().split()))
    mat.append(s)
#print(mat)
if r==1 and c==1:
    print(6)
else:
    cost=2*(r*c)
    for i in range(0,r):
        for j in range(0,c):
            if i==0 and j==0:
                cost=cost+2*(mat[i][j])
                if mat[i][j]-mat[i][j+1]>0:
                    cost+=(mat[i][j]-mat[i][j+1])
                if mat[i][j]-mat[i+1][j]>0:
                    cost+=(mat[i][j]-mat[i+1][j])
                #print("1stcornor")
                #1st cornor case clockwise
            elif i==0 and j==c-1:
                cost=cost+2*(mat[i][j])
                if mat[i][j]-mat[i][j-1]>0:
                    cost+=(mat[i][j]-mat[i][j-1])
                if mat[i][j]-mat[i+1][j]>0:
                    cost+=(mat[i][j]-mat[i+1][j])
                #print("2nd cornor")
                #2nd cornor case clockwise
            elif i==r-1 and j==c-1:
                cost=cost+2*(mat[i][j])
                if mat[i][j]-mat[i-1][j]>0:
                    cost+=(mat[i][j]-mat[i-1][j])
                if mat[i][j]-mat[i][j-1]>0:
                    cost+=(mat[i][j]-mat[i][j-1])
                #print("3rd cornor")
                #3rd cornor case cloockwise
            elif i==r-1 and j==0:
                cost=cost+2*(mat[i][j])
                if mat[i][j]-mat[i-1][j]>0:
                    cost+=(mat[i][j]-mat[i-1][j])
                if mat[i][j]-mat[i][j+1]>0:
                    cost+=(mat[i][j]-mat[i][j+1])
                #print("4th cornor")
                #4th cornor case clockwise
            elif i==0 and j!=c-1 and j!=0 :
                cost+=mat[i][j]
                if mat[i][j]-mat[i][j+1]>0:
                    cost+=(mat[i][j]-mat[i][j+1])
                if mat[i][j]-mat[i][j-1]>0:
                    cost+=(mat[i][j]-mat[i][j-1])
                if mat[i][j]-mat[i+1][j]>0:
                    cost+=(mat[i][j]-mat[i+1][j])
                #print("top row")
                #top row case
            elif i==r-1 and j!=c-1 and j!=0:
                cost+=mat[i][j]
                if mat[i][j]-mat[i][j+1]>0:
                    cost+=(mat[i][j]-mat[i][j+1])
                if mat[i][j]-mat[i][j-1]>0:
                    cost+=(mat[i][j]-mat[i][j-1])
                if mat[i][j]-mat[i-1][j]>0:
                    cost+=mat[i][j]-mat[i-1][j]
                #print("bottom row")
                #bottom row case
            elif j==0 and i!=0 and i!=r-1:
                cost+=mat[i][j]
                if mat[i][j]-mat[i-1][j]>0:
                    cost+=(mat[i][j]-mat[i-1][j])
                if mat[i][j]-mat[i+1][j]>0:
                    cost+=(mat[i][j]-mat[i+1][j])
                if mat[i][j]-mat[i][j+1]>0:
                    cost+=mat[i][j]-mat[i][j+1]
                #print("left col")
                #left col case
            elif j==c-1 and i!=0 and i!=r-1:
                cost+=mat[i][j]
                if mat[i][j]-mat[i+1][j]>0:
                    cost+=(mat[i][j]-mat[i+1][j])
                if mat[i][j]-mat[i-1][j]>0:
                    cost+=(mat[i][j]-mat[i-1][j])
                if mat[i][j]-mat[i][j-1]>0:
                    cost+=mat[i][j]-mat[i][j-1]
                #print("right col")
                #right col case
            else:
                if mat[i][j]-mat[i+1][j]>0:
                    cost+=(mat[i][j]-mat[i+1][j])
                if mat[i][j]-mat[i-1][j]>0:
                    cost+=(mat[i][j]-mat[i-1][j])
                if mat[i][j]-mat[i][j-1]>0:
                    cost+=(mat[i][j]-mat[i][j-1])
                if mat[i][j]-mat[i][j+1]>0:
                    cost+=(mat[i][j]-mat[i][j+1])
                #print("middle")
                    #middle"""
    print(cost)
