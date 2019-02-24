n,kk=map(int,input().split())
#print(n)
#print(kk)
s=list(map(int,input().split()))
'''#print(s)
use=[]
ctr=0
for i in range(0,len(s)):
    for j in range(0,len(s)-i):
        use.append([])
        for k in range(i,len(s)-j):
            #print(s[k],end=' ')
            use[ctr].append(s[k])
        ctr+=1
        #print()
#print(use)
for i in range(0,len(use)):
    if len(use[i])== kk :
        print(max(use[i]),end=' ')'''

for i in range(0,len(s)):
    if i<len(s)-kk +1:
        use=[]
        for j in range(i,i+kk):
            #print(s[j],end=' ')
            use.append(s[j])
        print(max(use),end=' ')
        #print(use)
        #print()
        
