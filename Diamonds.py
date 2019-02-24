t=int(input())
for i in range(0,t):
    z=input()
    n,m=z.split()
    n=int(n)
    m=int(m)
    pat=[]
    for j in range(0,n):
        y=input()
        pat.append([])
        for k in range(0,len(y)):
            if y[k]==' ':
                pass
            else:
                pat[j].append(y[k])
    #print(pat)
    '''for j in range(0,len(pat)):
        for k in range(0,len(pat[j])):
            print(pat[j][k],end=' ')
        print()'''
    ctr=0
    for j in range(0,len(pat)):
        if j<len(pat)-1:
            for k in range(0,len(pat[j])):
                if k<len(pat[j])-1:
                    if pat[j][k]=='/' :
                        if pat[j][k+1]=='\\' :
                            if pat[j+1][k]=='\\' :
                                if pat[j+1][k+1]=='/' :
                                    ctr+=1
    print(ctr)
