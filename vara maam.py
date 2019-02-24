def toString(List):
    return ''.join(List) 
def permute(a, l, r): 
    if l==r:
        b=list(a)
        ll.append(b)
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]
t=int(input())
for i in range(0,t):
    ll=[]
    string=input()
    n = len(string) 
    a = list(string) 
    permute(a, 0, n-1)
    #for i in range(0,len(ll)):
      #print(ll[i])
    #print(ll)
    ll.sort()
    if ll[0]==ll[1]:
        print("no answer")
    else:
        for i in range(0,len(ll)):
            if ll[i]==a :
                ans=''
                for j in range(0,len(ll[i])):
                    ans+=ll[i][j]
                print(ans)
                break
    
