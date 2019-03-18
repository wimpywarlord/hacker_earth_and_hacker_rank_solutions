'''
# DUE TO IMPOROPER EXPLAINATION AND CARELESS READING I MISS INTERPRETED THE
# QUESTION
import copy
for i in range(int(input())):
    n=int(input())
    mat=[]
    for j in range(n):
        s=input()
        mat.append(s)
    #print(mat)
    m=len(mat[0])
    use=[]
    for k in range(0,m):
        use.append([])
        for j in range(0,n):
            use[k].append(mat[j][k])
    print(use)
    use2=copy.deepcopy(use)
    use3=copy.deepcopy(use)
    print(use2)
    for j in range(0,len(use2)):
        use2[j].sort()
        use3[j].sort(reverse=True)
    print(use2)
    flag=0
    for j in range(0,m):
        if use2[j]!=use[j] and use3[j]!=use[j]:
            flag=1
            break
    if flag==1:
        print("NO")
    else:
        print("YES")

============================================================================
        
'''
'''
import copy
for i in range(int(input())):
    n=int(input())
    mat=[]
    for j in range(n):
        temp=list(input())
        mat.append(temp)
    print(mat)
    finaluse=''
    for j in range(n):
        for k in range(len(mat[j])):
            finaluse+=mat[j][k]
    #print(finaluse)
    sorted_finaluse=sorted(finaluse)
    sorted_finaluse="".join(sorted_finaluse)
    print(sorted_finaluse)
    flag=0
    for j in range(0,len(sorted_finaluse)):
        mainflag1=0
        for k in range(0,n):
            mainflag2=0
            found=0
            for f in range(0,len(mat[k])):
                print(sorted_finaluse[j])
                if j==0:
                    if sorted_finaluse[j]==mat[k][f]:
                        print("$")
                        pos=k
                        found=1
                        break
                else:
                    if sorted_finaluse[j]==mat[k][f] and pos!=k:
                        print(sorted_finaluse[j],mat[k][f],pos)
                        flag=1
                        mainflag1=1
                        mainflag2=1
                        break
                    elif sorted_finaluse[j]==mat[k][j] and pos==k:
                        pos=k
                        found=1
                        break
            if found==1:
                break
            if mainflag2==1:
                break
        if mainflag1==1:
            break
    if flag==1:
        print("NO")
    else:
        print("YES")

'''
'''
for i in range(int(input())):
    mat=''
    n=int(input())
    for j in range(n):
        s=input()
        mat+=s
    print(mat)
    use1=list(mat)
    use2=sorted(use1)
    print(use2)
    main_flag=0
    ctr=0
    ptr=0
    for j in range(0,len(use2)):
        pos=0
        flag=0
        for k in range(0,len(mat)):
            print(use2[j],mat[k],ctr*n,k+1,(ctr+1)*n)
            if use2[j]==mat[k] and ctr*n<k+1<=(ctr+1)*n:
                print("star")
                break
            elif use2[j]==mat[k] and ctr*n>k+1 or k+1>(ctr+1)*n:
                print("yolo")
                flag=1
                main_flag=1
                break
        if (j+1)%n==0:
            ctr+=1
        if main_flag==1:
            break
    if main_flag==1:
        print("NO")
    else:
        print("YES")
'''        

T = int(input())

all_grids = []
for t in range(T):
    N = int(input())
    n = [''.join(sorted(input().strip())) for i in range(N)]
    all_grids.append([N, n])

def check_condition(grid):
    answer = 'YES'
    for i in range(grid[0] - 1):
        for j in range(grid[0]):
            if grid[1][i][j] > grid[1][i+1][j]:
                answer = 'NO'
                return answer
    return answer

answers = []

for grid in all_grids:
    answers.append(check_condition(grid))

print('\n'.join(answers))
