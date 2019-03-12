n,p=map(int,input().split())
use=[]
for i in range(0,p):
    s=list(map(int,input().split()))
    flag1=0
    flag2=0
    for j in range(0,len(use)):
        if s[0] in use[j]:
            flag1=1
            use[j].append(s[1])
        if s[1] in use[j]:
            flag2=1
            use[j].append(s[0])
    if flag1==0 and flag2==0:
        use.append([s[0],s[1]])

for i in range(n):
    flag=0
    for j in range(0,len(use)):
        if i in use[j]:
            flag=1
    if flag==0:
        use.append([i])
for i in range(0,len(use)):
    use[i]=(set(use[i]))
#print(use)
#print()
final=[]
check=[]
for i in range(0,len(use)):
    temp=[]
    flag=0
    temp.append(use[i])
    for j in range(i+1,len(use)):
        if len(use[i].intersection(use[j]))!=0:
            temp.append(use[j])
            check.append(j)
            flag=1
    #print(check)
    if i not in check :  
        final.append(list(set().union(*temp)))
        check.append(i)
    if flag==0 and  i not in check:
        final.append(use[i])    
#print(final)                  
sum=0
for i in range(0,len(final)):
    #print(sum)
    for j in range(i+1,len(final)):
        sum+=len(final[i])*len(final[j])
print(sum)
