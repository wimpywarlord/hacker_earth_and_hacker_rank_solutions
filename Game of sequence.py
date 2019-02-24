t=int(input())
for i in range(0,t):
    n=int(input())
    z=input()
    l=z.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    d={}
    for j in range(0,len(l)):
        d[l[j]]=0
    for j in range(0,len(l)):
        d[l[j]]+=1
    #print(d)
    v=list(d.keys())
    #print(len(v))
    if len(v)%2==0:
        print("Q")
    else:
        print("P")
