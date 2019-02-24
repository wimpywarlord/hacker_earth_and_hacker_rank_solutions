x=input()
t,r,g,b=x.split()
t=int(t)
r=int(r)
g=int(g)
b=int(b)
rlist=[]
blist=[]
glist=[]
for i in range(0,t):
    rlist.append(0)
    glist.append(0)
    blist.append(0)
for i in range(r,t,2*r):
   
    for j in range(i,i+r):
      if j<t:
        rlist[j]=1
      else:
        break
    
for i in range(g,t,2*g):
   
    for j in range(i,i+g):
       if j<t:
        glist[j]=3
       else:
        break
    
for i in range(b,t,2*b):
    for j in range(i,i+b):
      if j<t:
        blist[j]=5
      else:
        break


for l in range(0,t):
    summ=0
    summ=rlist[l]+glist[l]+blist[l]
    rlist[l]=summ

cl=[]
for i in range(0,8):
    cl.append(0)
for m in range(0,t):
    if rlist[m]==1:
        cl[0]=cl[0]+1
    elif rlist[m]==3:
        cl[1]=cl[1]+1
    elif rlist[m]==5:
        cl[2]=cl[2]+1
    elif rlist[m]==4:
        cl[3]=cl[3]+1
    elif rlist[m]==8:
        cl[4]+=1
    elif rlist[m]==6:
        cl[5]+=1
    elif rlist[m]==9:
        cl[6]+=1
    elif rlist[m]==0:
        cl[7]+=1

cl=map(str,cl)
yy=" ".join(cl)
print(yy)


