for _ in range(int(input())):
    num = int(input())
    List = list(map(int, input().split()))
    diff,prev,diff = 0,0,0
    
    # increasing
    prev = i = List[0]
    for curr in List[1:]:
        if prev <= curr:
            diff = max(diff, curr-i)
        else:
            i = curr
        prev = curr
    
    # decreasing
    prev = i = List[0]
    for curr in List[1:]:
        if prev >= curr:
            diff = max(diff, i-curr)
        else:
            i = curr
        prev = curr
    print(diff)
