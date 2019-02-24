n=int(input())
l=list(input())
use=[]
for i in range(0,len(l)):
    if i<len(l)-2:
        if l[i]=='0' and l[i+1]=='1' and l[i+2]=='0':
            use.append(i)
#print(use)       
for i in range(0,len(use)):
    x=len(use)
    for j in range(0,x):
        if j!=x-1:  
            if (use[j+1]-use[j])<=2:
                del use[j+1]
                break
print(len(use))
