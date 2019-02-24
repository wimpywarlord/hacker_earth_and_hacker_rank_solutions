n=int(input())
d1={}
d2={}
l1=[]
for i in range(0,n):
  N,T=[str(x) for x in input().split()]
  d1[int(T)]=N
  d2[N]=int(T)
  l1.append(int(T))
l1.sort()
l1.reverse()
for i in range(0,3):
  l2=l1[i]
  print(d1[l2])
