'''t=int(input())
for i in range(0,t):
    n=int(input())
    l=list(map(int,input().split()))
    inv=0
    for j in range(0,len(l)):
        for k in range(j+1,len(l)):
            if l[j]>l[k]:
                inv+=1
    print(inv)
    if inv%2==0:
        print("YES")
    else:
        print("NO")'''
t = int(input())
for i in range(t):
    a = 0
    n = int(input())
    li = [int(x) for x in input().split()]
    for j in range(n):
        for k in range(j+1,n):
            if li[j]>li[k]:
                a += 1
    if a%2 == 0:
        print("YES")
    else:
        print("NO")
