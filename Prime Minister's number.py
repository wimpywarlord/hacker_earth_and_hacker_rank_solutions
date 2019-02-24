s=input()
l,r=s.split()
l=int(l)
r=int(r)
def prime(a):
    for j in range(2,a):
        if a%j==0:
            return 0
    return 1
for i in range(l,r+1):
    if prime(i)==1:
        f=[]
        while i>0:
            w=i%10
            f.append(w)
            i=i//10
        summ=0
        for j in range(0,len(f)):
            summ+=f[j]
        if prime(summ)==1 or summ==2:
            for k in range(len(f)-1,-1,-1):
                print(f[k],end='')
            print(end=' ')
        
        
            
    
