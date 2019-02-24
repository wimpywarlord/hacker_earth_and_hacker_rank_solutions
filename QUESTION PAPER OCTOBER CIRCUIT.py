t=int(input())
for i in range(0,t):
    x=input()
    n,a,b=x.split()
    n=int(n)
    a=int(a)
    b=int(b)
    from itertools import product
    final=[]
    for roll in product([0,a,-b], repeat = n):
        final.append(list(roll))
        print(roll)
    print(final)
    ans=set()
    for i in range(0,len(final)):
        marks=0
        for j in range(0,len(final[i])):
            marks+=final[i][j]
        ans.add(marks)
    print(len(ans))

 
