t=int(input()) 
def computeGCD(x, y): 
    if x==0:
        return x
    return computeGCD(y%x,x)
def check(g):
    if g%2==0:
        return 1
    else:
        return 2
for i in range(t):
    x=input()
    n,q=x.split()
    n=int(n)
    q=int(q)
    y=input()
    arr=y.split()
    for j in range(0,len(arr)):
        arr[j]=int(arr[j])
    for j in range(q):
        z=input()
        k,l,r=z.split()
        k=int(k)
        l=int(l)
        r=int(r)
        if k==0:
            ctr1=0
            ppp=0
            for k in range(l-1,r):
                if check(arr[k])==1:
                    ctr1+=1
            if ctr1==0 : 
                print(0)
            elif ctr1==len(arr):
                print(1)
            else:
                aaa=r-l+1
                ppp=computeGCD(ctr2,aaa)
                ctr1=ctr1//ppp
                aaa=aaa//ppp
                print(ctr1,aaa)
        elif k==1:
            ctr2=0
            ppp=0
            for k in range(l-1,r):
                if check(arr[k])==2:
                    ctr2+=1
            if ctr2==0 : 
                print(0)
            elif ctr2==len(arr):
                print(1)
            else:
                aaa=r-l+1
                ppp=computeGCD(ctr2,aaa)
                print(ppp)
                #print(ppp)
                ctr2=ctr2//ppp
                aaa=aaa//ppp
                print(ctr2,aaa)
                
