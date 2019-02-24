N=int(input())
c=input()
mat=c.split()
cal=[]
for i in range(0,N):
    count=0
    a=0
    s=i
    for j in range(0,N):
        a=1+j
        if (s+a)<=N:
            for k in range(0,a):
                print(int(mat[s]),end=' ')
                count=count+int(mat[s])
                s=s+1
            print()
    cal.append(count)
print(max(cal))        
