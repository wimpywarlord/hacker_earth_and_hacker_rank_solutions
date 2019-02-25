for l in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    x = []
    y = []
    for i in range(n):
        x.append(li[i] + i)
        y.append(li[i] - i)
    print(max(max(x) - min(x), max(y) - min(y)))
