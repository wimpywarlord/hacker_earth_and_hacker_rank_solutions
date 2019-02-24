n=int(input())
for i in range(0,n):
    for j in range(1,n-i):
        print(end=' ')

    for j in range(n-i -1,n):
        print(end='#')
    print()
        
