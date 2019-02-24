n=int(input())
x=input()
a=x.split()
for i in range(0,len(a)):
    a[i]=int(a[i])
maxsofar=0
maxendhere=0
for j in range(0,len(a)):
    maxendhere=maxendhere+a[j]
    if maxsofar<maxendhere:
        maxsofar=maxendhere
    if maxendhere<0:
        maxendhere=0
print(maxsofar)
    
