n,q=map(int,input().split())
#print(n)
#print(q)
arr=list(map(int,input().split()))
print(arr)
for i in range(0,q):
    l,r=map(int,input().split())
    print(l)
    print(r)
    if i==0:
        l=l-1
        use=[]
        #print(l,r,end=' ')
        #print()
        imp=[]
        for i in range(l,r):
            imp.append(arr[i])
        imp.sort()
        print(imp)
        for i in range(l,r):
            z=0
            flag=0
            ctr=0
            for j in range(l,r):
                if imp[ctr]==arr[j] and flag==0:
                    pass
                else:
                    flag=1
                    z+=abs(arr[i]-arr[j])
                ctr+=1
                    
                #JUST THINK OF THIS CONDITION WISELY
            use.append(z)
        last=min(use)
        print(last)
        print(use)
    else:
        l=((l+last-1)%n)+1
        r=((r+last-1)%n)+1
        print(l,r,end=' ')
        print()
        use=[]
        imp=[]
        for i in range(l-1,r):
            imp.append(arr[i])
        imp.sort()
        print(imp)
        for i in range(l-1,r):
            z=0
            flag=0
            ctr=0
            for j in range(l-1,r):
                if imp[ctr]==arr[j] and flag==0:
                    pass
                else:
                    flag=1
                    z+=abs(arr[i]-arr[j])
                ctr+=1
                #JUST THINK OF THIS CONDITION WISELY
            use.append(z)
        print(use)
        last=min(use)
        print(last)
