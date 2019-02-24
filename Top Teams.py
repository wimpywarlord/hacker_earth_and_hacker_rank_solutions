t=int(input())
for i in range(0,t):
    use=[]
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    z=list(map(int,input().split()))
    #print(x)
    #print(y)
    #print(z)
    use.append(x)
    use.append(y)
    use.append(z)
    use.sort(reverse=True)
    #print(use)
    flag=0
    for i in range(0,len(use)):
        if i!=len(use)-1:
            if use[i][0]<use[i+1][0] or use[i][1]<use[i+1][1] or use[i][2]<use[i+1][2]:
                flag=1
            elif use[i][0]==use[i+1][0] and use[i][1]==use[i+1][1] and use[i][2]==use[i+1][2]:
                flag=1
    if flag==1:
        print("no")
    else:
        print("yes")
                
            
            
    
        
