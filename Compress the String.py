t=int(input())
b=[1,2,3,4,5,6,7,8,9,-1]
a=['a','e','i','o','u','0']
for i in range(0,t):
    n=int(input())
    z=input()
    l=[]
    for i in range(0,len(z)):
        l.append(z[i])
    l[0]=chr(ord(l[0]) - 32)
    for i in range(1,len(l)):
        if l[i] in a:
            if l[i-1] in a and (l[i-1]==l[i] or l[i-1]==0):
                l[i]='0'
    print(l)
    for i in range(0,len(l)):
        x=len(l)
        for j in range(0,x):
            if l[j]=='0':
                del l[j]
                break
    print(l)
    cc=0
    ee=[]
    ff=[]
    for j in range(1,len(l)):
        if l[j] not in a:
            cc=cc+1
            ff.append(j)
        elif (l[j] in a) and (cc!=0):
            for k in range(0,len(ff)):
                l[ff[k]]=cc  
            ee.append(cc)
            cc=0
    print(l)
    for i in range(1,len(l)):
        if l[i-1] in b and l[i] in b :
            l[i]=-1
    for i in range(0,len(l)):
        x=len(l)
        for j in range(0,x):
            if l[j]==-1:
                del l[j]
                break
    ctr=0
    print(l)
    for i in range(0,len(l)):
        if l[i] in b:
            l[i]=ee[ctr]
            ctr+=1
    for i in range(0,len(l)):
        l[i]=str(l[i])
    
    print("".join(l))

            
        











                
