n=int(input())
l=[]
for i in  range(n):
    z=int(input())
    l.append(z)
for i in range(0,len(l)):
    x=len(l)
    #print(l)
    for j in range(0,x):
        if l[j]==0 and j!=0:
            del l[j]
            del l[j-1]
            break
            
print(sum(l))
