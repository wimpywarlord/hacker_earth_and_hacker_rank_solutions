t=int(input())
ll=[]
def permute(a, l, r): 
    if l==r: 
        ll.append(a)
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] # backtrack 
for i in range(0,t):
    s=input()
    n = len(s) 
    a = list(s) 
    permute(a, 0, n-1)
    print(ll)
    use=[]
    for j in range(0,len(ll)):
        temp=''
        for k in range(0,len(ll[j])):
            temp+=ll[j][k]
        use.append(temp)
    print(use)
    use.sort()
    for j in range(0,len(use)):
        if use[j]==s:
            print(use[j+1])
            break
    
