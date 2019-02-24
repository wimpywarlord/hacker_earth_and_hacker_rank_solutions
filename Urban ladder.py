a=input()
n,l,m=a.split()
b=[]

x=input()
b=x.split()
for i in range(0,int(n)):
    b[i]=int(b[i])




count=0
bfalg=0
for i in range(0,len(b)):
    flag=0
    for j in range(i,i+int(m)):
      if i + int(m) < len(b):
        if b[j] > int(l):
            flag=1
        else:
            pass
      elif i + int(m) >= len(b):
         bfalg=1
         break
        
      print(b[j])
    print(flag)
    if bfalg==1:
       break
    else:
       if flag==1:
           pass
       else :
           count+=1
    print()
print()    
print(count)
