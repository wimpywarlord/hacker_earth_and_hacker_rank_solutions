s = int(input().strip())
ar = [int(temp) for temp in input().strip().split(' ')]

def insertionSort(ar, i):
    new = sorted(ar[:i+1]) + ar[i+1:]
    return ' '.join(str(k) for k in new)

for i in range(1, s):
    print(insertionSort(ar, i))

