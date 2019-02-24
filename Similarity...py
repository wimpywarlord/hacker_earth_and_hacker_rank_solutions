t=int(input())
for i in range(0,t):
    s1=input()
    s2=input()
    s11=[]
    s22=[]
    for j in range(0,len(s1)):
        s11.append(s1[j])
    for j in range(0,len(s2)):
        s22.append(s2[j])
        #print(s11)
    #print(s22)
    for j in range(0,len(s11)):
        for k in range(0,len(s22)):
            if s11[j]==s22[k]:
                s11[j]=0
                s22[k]=0
    ctr=0
    #print(s11)
    #print(s22)
    for j in range(0,len(s11)):
        if s11[j]!=0:
            ctr+=1
    for j in range(0,len(s22)):
        if s22[j]!=0:
            ctr+=1
    print(ctr)
    

    
