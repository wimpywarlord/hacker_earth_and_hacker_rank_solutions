n =int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
#print(l)
s=input()
ptr=0
while len(l)>1:
    for i in range(0,len(s)):
        if ptr>=len(l):
            ptr=0
        if len(l)==1:
            break
        elif s[i]=='a':
            ptr+=1
            pass
        elif s[i]=='b':
            del l[ptr]
    #print(l)
print(l[0])
