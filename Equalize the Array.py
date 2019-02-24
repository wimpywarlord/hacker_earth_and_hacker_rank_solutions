n=int(input())
z=input()
l=z.split()
d={}
for i in range(0,len(l)):
    d[l[i]]=0
for i in range(0,len(l)):
    d[l[i]]+=1
#print(d)
values=list(d.values())
#print(values)
summ=0
for i in range(0,len(values)):
    summ+=values[i]
ans=summ-max(values)
print(ans)
