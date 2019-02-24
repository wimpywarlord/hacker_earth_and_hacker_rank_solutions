n=int(input())

for i in range(0,n):
    ctr=0
    x=int(input())
    for j in range(3,x):
        if j%3==0 or j%5==0:
            ctr+=j
    print(ctr)
