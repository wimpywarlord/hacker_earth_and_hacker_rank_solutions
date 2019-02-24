while 1:    
    b=[]
    n=int(input())
    if not n:
        break    
    else:
        
        while n>0:
            g=n%2
            b.append(g)
            n=n//2
        print(sum(b))
    
