n=int(input())
s=input()
ss=[]
ll=[]
for i in range(0,len(s)):
    ss.append(s[i])
    ll.append(s[i])

print(ll)
t=[]
rr=0
for l in range(0,len(ll)):
    if l!=len(ll)-1:
        if ll[l]=='v' and ll[l+1]=='v':
            rr+=1
            t.append(l)
print(t)
print(rr)
for e in range(0,rr):
    yy=len(ll)
    print(yy)
    for k in range(0,yy):
        if k!=len(ll)-1:
            if ll[k]=='v' and ll[k+1]=='v':

                print(ll[k])
                del ll[k]
                print(ll[k])
                del ll[k]
                print(ll)  
                break
for i in range(0,len(ll)):
    for j in range(0,len(t)):
        if ll[i]==t[j]:
            ll.insert(j,'w')
print(ll)






c=0
for j in range (0,len(ss)):
    if ss[j]=='w':
        c+=1
print(c)
for i in range(0,c):
    xx=len(ss)
    for j in range(0,xx):
        if ss[j]=='w':
            del ss[j]
            ss.insert(j,'v')
            ss.insert(j,'v')
         
print(ss)
print(len(ss))
