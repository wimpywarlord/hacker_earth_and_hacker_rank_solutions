s=input()
c=input()
p=int(input())
b=[]
for  i in range(0,len(s)):
    for j in range(i,len(s)):
        b.append([])
        for k in range(j,p+j):
            if k<len(s):
                b[j].append(s[k])
                print(s[k],end=' ')
                
        print()
    break
for i in range(1,p+1):    
    del b[len(s)-i]
print(b)
listoff=[]

for i in b:
    count=0
    for j in i:
        if j==c:
            count+=1
    listoff.append(count)
print(listoff)
maxofor=max(listoff)
copy=s
listofff=[]
for y in range(0,len(s)):
    s=s[:y]+c+s[y:]
    b=[]
    for  i in range(0,len(s)):
        for j in range(i,len(s)):
            b.append([])
            for k in range(j,p+j):
                if k<len(s):
                    b[j].append(s[k])
                    print(s[k],end=' ')        
            print()
        break
    listoff=[]
    for i in b:
        count=0
        for j in i:
            if j==c:
                count+=1
        listoff.append(count)
    print(listoff)
    listofff.append(listoff)
    for i in range(1,p+1):    
        del b[len(s)-i]       
    print(b)
    print(s)
    s=copy
flag=0
print(listofff)
for i in range(len(listofff)-1,-1,-1):
    if max(listofff[i])==maxofor+1:
        if i == 0 :
            print("0")
            flag=1
        if i== len(listofff)-1:
            flag=1
            print(i+1)
        else:
            print(i)
            flag=1
        break
if flag==0:
    print("-1")
    
                
#print(listofff)
# FIRST OFF ALL THE QUESTION MUST BE UNDERSTOOD
# WE HAVE TO FIND THE MAXIMUM INDEX WHERE IF WE INSERT D THEN WE MUST GET THE
# MAXIMUM FREQUENCY TO BE Z + 1 where z is the previous maximum frequency.
