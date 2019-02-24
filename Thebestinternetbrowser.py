t=int(input())
for i in range(0,t):
    a=input()
    c=len(a)
    b=a.split(".")
    counter=0
    for j in b[1]:
        
        x=ord(j)
        
        if x==97 or x==101 or x==105 or x==111 or x==117:
             counter+=1
            
        else:
             pass
    print(len(a) - 4 - counter,end='')
    print("/",end='')
    print(c)
    
