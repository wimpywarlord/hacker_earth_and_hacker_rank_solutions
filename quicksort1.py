from itertools import chain

n = int(input())
p, *a = map(int, input().split())
first, equal, last = [], [p], []
for i in a:
    if i < p:
        first.append(i)
    elif i > p:
        last.append(i)
    else:
        equal.append(i)
print(*chain(first, equal, last))
