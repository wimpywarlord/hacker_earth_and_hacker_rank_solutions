t=int(input())
for i in range(0,t):
    x=input()
    a,b=x.split()
    a=int(a)
    b=int(b)
    num=[]
    count=0
    for j in range(a,b+1):
        num.append([])
        while j>0:
            y=j%10
            num[count].insert(0,y)
            j=j//10
        count+=1
    palin=0
    for k in range(0,len(num)):
            b=num[k][::-1]
            if b==num[k]:
                
                palin+=1
    print(palin)      
    
