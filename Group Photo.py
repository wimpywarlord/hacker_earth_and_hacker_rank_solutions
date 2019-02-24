'''n=int(input())
wl=[]
hl=[]
for i in range(0,n):
    z=input()
    w,h=z.split()
    w=int(w)
    h=int(h)
    wl.append(w)
    hl.append(h)
#print(wl)
#print(hl)
for i in range(0,n):
    usewl=[]
    usehl=[]
    for j in range(0,n):
        if j!=i:
            usewl.append(wl[j])
            usehl.append(hl[j])
    summ=0
    #print(usehl)
    #print(usewl)
    for j in range(0,len(usewl)):
        summ+=usewl[j]
        #print(summ)
    print(summ*max(usehl),end=' ')'''
n = int(input())
if n == 1:
    print(0)
    quit()
w = []
h = []
for _ in range(n):
    x, y = map(int, input().split())
    w.append(x)
    h.append(y)
W = sum(w)
H1, H2 = sorted(h, reverse=True)[:2]
r = [(W - w[i]) * (H2 if h[i] == H1 else H1) for i in range(n)]
print(*r)    
