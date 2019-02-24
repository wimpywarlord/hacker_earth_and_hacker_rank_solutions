b=input()
a=[]
for l in range(0,len(b)):
    a.append(b[l])
for i in range(len(a)-1,-1,-1):
    if a[i]=='.':
        ex=[]
        for j in range(i+1,len(a)):
             ex.append(a[j])
             a[j]='0'
        
        #print(a)
    if a[i]=='\\' :
        file=[]
        for k in range(i+1,len(a)):
           if a[k]=='.':
               break
           else:
               file.append(a[k])
               a[k]='0'
        
        break
print("Path:",end=" ")
for n  in range(0,len(a)):
    if a[n]=='0':
        break
    else :
        print(a[n],end='')
print()
print("File name:",end=" ")
for n  in range(0,len(file)):
    print(file[n],end='')
print()
print("Extension:",end=" ")
for n  in range(0,len(ex)):
    print(ex[n],end='')
print()
