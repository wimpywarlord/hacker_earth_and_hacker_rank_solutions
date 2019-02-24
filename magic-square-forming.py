lmain=[]
for i in range(0,3):
    s=input()
    lpart=s.split()
    for j in range(0,len(lpart)):
        lpart[j]=int(lpart[j])
    lmain.append(lpart)
pre = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
costl=[]
for i in range(0,len(pre)):
    cost=0
    for j in range(0,len(pre[i])):
        for k in range(0,len(pre[i][j])):
            cost+=abs(pre[i][j][k]-lmain[j][k])
    costl.append(cost)
finder=min(costl)
print(finder)
            
        
