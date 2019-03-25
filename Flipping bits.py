for i in range(int(input())):
    n=int(input())
    bin_n=list(bin(n))
    #print(bin_n)
    del bin_n[0]
    del bin_n[0]
    for j in range(0,32-len(bin_n)):
        bin_n.insert(0,'0')
    #print(bin_n)
    use=[0]*32
    for j in range(0,len(bin_n)):
        if bin_n[j]=='0':
            use[j]=1
        if bin_n[j]=='1':
            use[j]=0
    #print(use)
    ans=0
    ctr=0
    for j in range(len(use)-1,-1,-1):
        ans+=int(use[j])*(2**(ctr))
        ctr+=1
    print(ans)
