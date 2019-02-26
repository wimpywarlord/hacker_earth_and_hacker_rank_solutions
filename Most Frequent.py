'''from collections import defaultdict
n=int(input())
d=defaultdict(int)
a=list(map(int,input().split()))
for i in range(n):
    d[a[i]]+=1
v=list(d.values())
for i in range(n):
    if d[a[i]]==max(v):
        print(a[i])
        break
'''
n=input()
l=sorted(input().split(" "))
l=list(map(int,l))
p=list(map(l.count,l))
print(l[p.index(max(p))])
