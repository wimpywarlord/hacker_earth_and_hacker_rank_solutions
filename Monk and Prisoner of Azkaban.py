n=int(input())
s=input()
l=s.split()
for i in range(0,len(l)):
    l[i]=int(l[i])
#print(l)
usemax=max(l)
x=[]
y=[]
#LHS
for i in range(0,len(l)):
    if i==0:
        x.append(-1)
    elif l[i]==usemax:
        x.append(-1)
    else:
        flag=0
        for j in range(i-1,-1,-1):
            if l[j]>l[i]:
                x.append(j+1)
                flag=1
                break
        if flag==0:
            x.append(-1)
            
#RHS       
for i in range(0,len(l)):
    if l[i]==usemax:
        y.append(-1)
    else:
        flag=0
        for j in range(i+1,len(l)):
            if l[j]>l[i]:
                y.append(j+1)
                flag=1
                break
        if flag==0:
            y.append(-1)

#print(x)
#print(y)
for i in range(0,len(x)):
    print(x[i]+y[i],end=' ')
    
