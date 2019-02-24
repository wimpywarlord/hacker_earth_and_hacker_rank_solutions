n=int(input())
s=list(input())
d={}
for i in range(0,n):
    d[s[i]]=0
for i in range(0,n):
    d[s[i]]+=1
#print(d)
keyuse=list(d.keys())
value=list(d.values())
uselist=[]
uselistctr=0
for i in range(0,len(value)):
    if value[i]>n//4:
        uselist.append([])
        uselist[uselistctr].append(keyuse[i])
        uselist[uselistctr].append(value[i]-n//4)
        uselistctr+=1
#print(uselist)
sub=[]
for i in range(0,n):
    for j in range(0,n-i):
        temp=''
        for k in range(i,n-j):
            #print(s[k],end='')
            temp+=s[k]
        #print()
        sub.append(temp)
#print(sub)
ans=[]
for i in range(0,(n*(n+1))//2):
    tempdict={}
    for j in range(0,len(sub[i])):
        tempdict[sub[i][j]]=0
    for j in range(0,len(sub[i])):
        tempdict[sub[i][j]]+=1
    #print(tempdict)
    tempdictkey=list(tempdict.keys())
    tempdictval=list(tempdict.values())
    flag=0
    for j in range(0,len(uselist)):
        if uselist[j][0] in tempdictkey:
            #print(tempdict[uselist[j][0]],uselist[j][1])
            if tempdict[uselist[j][0]]!=uselist[j][1] or len(tempdictkey)<len(uselist):
                flag=1
                break
        else:
            flag=1
    if flag==0:
        summ=0
        for j in range(0,len(tempdictval)):
            summ+=tempdictval[j]
        ans.append(summ)
print(min(ans))
