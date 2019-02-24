n=int(input())
x=input()
a=x.split()
for i in range(0,len(a)):
    a[i]=int(a[i])
counter=0
for j in range(0,len(a)):
   if j<len(a)-1:
      if a[j]>a[j+1]:
          counter+=a[j]-a[j+1]+1 
          a[j+1]=a[j]+1           
   else:
      pass
print(counter)

