n=int(input())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
#print(s1)
#print(s2)
def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

l=[]
for p in permute(s1):
    b=list(p)
    l.append(b)
l.sort()
use=[]
for i in range(0,len(l)):
    if l[i] not in use:
        use.append(l[i])
use.sort()
print(use)
ans=0
for i in range(0,len(use)):
    if use[i]>=s2:
        ans=i
        break
print(ans%(10**9+7))
