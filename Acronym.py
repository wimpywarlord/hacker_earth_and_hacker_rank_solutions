n=int(input())
excep=[]
for i in range(0,n):
    x=input()
    excep.append(x)
print(excep)
m=int(input())
y=input()
l=y.split()
print(l)
final=[]
for i in excep:
    for j in l:
        if j==i:
            l.remove(j)
print(l)
final=[]
for i in range(0,len(l)):
    x=l[i]
    y=ord(x[0])-32
    final.append(chr(y))
    if i ==len(l)-1:
        pass
    else:
        final.append(".")
print(final)
ii=''
for i in final:
    ii+=str(i)
print(ii)
    
