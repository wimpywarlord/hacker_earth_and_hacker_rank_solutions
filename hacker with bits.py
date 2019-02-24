n=int(input())
x=input()
a=x.split()
for i in range(0,n):
    a[i]=int(a[i])
g=[]
flag=0
for j in range(0,n):    
    if a[j]==0:
        flag=1
        for k in range(0,n):
            if a[k]==1:
                temp=a[j]
                a[j]=a[k]
                a[k]=temp    
                print(a)
                u=[]
                counter=0
                a.append(0)
                for e in range(0,len(a)):
                    if a[e]==1:
                        counter+=1
                    elif a[e]==0 :
                        print(counter)
                        u.append(counter)
                        counter=0
                print(u)
                g.append(max(u))
                print(g)
                a=x.split()
                for z in range(0,n):
                    a[z]=int(a[z])
                print(a)
                print()
count=0
for h in range(0,len(a)):
    if a[h]==1:
        count+=1       
if count==len(a):
    print(len(a))    
elif not g:
    print("0")
else:
    print(max(g))
            
        
    
