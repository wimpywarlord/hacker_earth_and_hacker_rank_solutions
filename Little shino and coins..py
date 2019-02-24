u=int(input())
#print(u)
s=input()
l=list(s)
#print(l)
c=[]
check=0
for i in range(0,len(l)):
    ctr=len(l)
    for j in range(i,len(l)):
        c.append([])
        for k in range(i,len(l)):
            if k<ctr:
                #print(l[k],end=' ')
                c[check].append(l[k])           
            else:
                pass
        check+=1
        #print()
        ctr-=1

#print(c)
ans=0
for i in range(0,len(c)):
    #print()
    v=[]
    disctr=0
    for j in range(0,len(c[i])):
        #print(c[i][j])
        #print(v)
        if c[i][j] not in v:
            v.append(c[i][j])
            disctr+=1
    #print(disctr)      
    if disctr==u:
        #print("%")
        ans+=1
print(ans)
                   
            
            
