t=int(input())
for i in range(0,t):
    n=int(input())
    coco=[]
    for j in range(0,n):
        coco.append([])
        y=input()
        for k in range(0,len(y)):
            coco[j].append(y[k])
    print(coco)
    flag=0
    for j in range(0,n):
        ctr1=0
        ctr2=0
        for m  in range(0,j+1):
            for k in range(0,n):
                if coco[m][k]=='#':
                    ctr1+=1
        for v in range(j+1,n):
            for k in range(0,n):
                if coco[v][k]=='#':
                    ctr2+=1
        print(ctr1)
        print(ctr2)
        if ctr1==ctr2:
            flag=1
            break
    for j in range(0,n):
        ctr11=0
        ctr22=0
        for m in range(0,n):
            for k in range(0,j+1):
                if coco[m][k]=='#':
                    ctr11+=1
        for v in range(0,n):
            for k in range(j+1,n):
                if coco[v][k]=='#':
                    ctr22+=1
        if ctr11==ctr22:
            print("*")
            flag=1
            break
    if flag==1:
        print("YES")
    else:
        print("NO")
        
            
