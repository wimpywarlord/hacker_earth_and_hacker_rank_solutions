t=int(input())
for i in range(t):
    s=input()
    for n in range(1, len(s)+1):
        t = s[:n]
        l = [t]
        if t == s:
            print('NO')
            break
        while len(''.join(l)) < len(s):
            l.append(str(int(l[-1]) + 1))
        if ''.join(l) == s:
            print('YES', l[0])
            break

