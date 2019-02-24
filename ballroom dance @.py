<center>
<pre>
nb=int(input())
x=input()
bs=x.split()
for i in range(0,len(bs)):
    bs[i]=int(bs[i])

ng=int(input())
y=input()
gs=y.split()
for j in range(0,len(gs)):
    gs[j]=int(gs[j])
#bs.sort()
#gs.sort()

print(bs)
print(gs)
count=0
c=[]
for k in range(0,len(bs)):
    c.append([])
    for l in range(0,len(gs)) :
        if abs(bs[k]-gs[l])<=1 and bs[k]!=-1000 and gs[l]!=-1000:
            c[k].append(bs[k])
            c[k].append(gs[l])
            bs[k]=-1000
            gs[l]=-1000
            count+=1
        
print(c)
print(count)
</pre>
<center>
