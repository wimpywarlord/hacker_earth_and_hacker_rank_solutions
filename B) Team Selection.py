n=int(input())
s1=input()
s2=input()
l1=s1.split()
l2=s2.split()
for j in range(0,len(l1)):
    l1[j]=int(l1[j])
for j in range(0,len(l2)):
    l2[j]=int(l2[j])
#print(l1)
#print(l2)
use=[]
ctr=0
for i in range(0,len(l1)):
    for j in range(0,len(l1)):
        if l1[j]>l1[i] and j>i:
            use.append([])
            use[ctr].append(l1[i])
            use[ctr].append(l1[j])
            ctr+=1
#print(use)
ans=[]
nctr=0
for i in range(0,len(use)):
    for j in range(0,len(l2)):
        if use[i][0]<l2[j] and use[i][1]<l2[j]:
            ans.append(use[i])
            #print(ans)
            #ans[nctr].append(l2[j])
            #nctr+=1
            #print(nctr)
print(len(ans))
