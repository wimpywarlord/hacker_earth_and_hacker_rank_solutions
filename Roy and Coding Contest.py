'''t=int(input())
for i in range(0,t):
    z=input()
    n,pd=z.split()
    n=int(n)
    pd=int(pd)
    use=1
    time=0
    if n>=pd:
        for j in range(0,pd):
            if use>=n:
                break
            else:    
                use+=(j)
                time+=1
        #print(use)
        #print(time)
        ans=time
        print(use)
        print(ans)
    else:
        print("BRUH")'''
# Roy and Coding Contest
 
def solve(N, M):
    if N == 1:
        return 0
    c = 0
    l = 1
    ans = 0
    while c < M:
        a = l
        l += c
        c += a
        ans += 1
        if l >= N:
            break
    if N <= 0:
        return ans
    else:
        ans += (N - l) // M
        if (N - l) % M > 0:
            ans += 1
        return ans
 
for t in range(int(input())):
    N, M = [int(_) for _ in input().split()]
    print(solve(N, M))
