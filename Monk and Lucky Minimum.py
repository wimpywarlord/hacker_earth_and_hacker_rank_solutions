t=int(input())
for i in range(0,t):
    n=int(input())
    s=input()
    l=s.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    l.sort()
    ctr=0
    for j in range(0,len(l)):
        if l[j]==min(l):
            ctr+=1
        else:
            break
    if ctr%2==0:
        print("Unlucky")
    else:
        print("Lucky")
