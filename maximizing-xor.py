l=int(input())
r=int(input())
if l==r:
    print(0)
else:
    use=[]
    for  i in range(l,r+1):
        for j in range(l,r+1):
            if i!=j:
                use.append(i^j)
    print(max(use))
