
#1 - D TUPLE
n=int(input())
t=()
for i in range(n):
    x=int(input())
    t=t+(x,)
print(t)
# 2-D TUPLE.
y=()
for i in range(2):
    m=()
    for j in range(2):
        x=int(input())
        m=m+(x,)
    y+=(m,)
print(y)
#TUPLE INTO LIST
l=[]
for i in t:
    l.append(i)
print(l)
#LIST INTO TUPLE
g=()
for j in l:
    g=g+(j,)
print(g)
#DICTIONARY
d=dict()
tt=[]
for i in range(3):
    x=input()
    tt.append([])
    for j in range(3):
        uu=int(input())
        tt[i].append(uu)
    d[x]=tt[i]
print(d)

