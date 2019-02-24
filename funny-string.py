q=int(input())
for i in range(0,q):
    z=list(input())
    for j in range(0,len(z)):
        z[j]=ord(z[j])
    #print(z)
    use=[]
    for j in range(1,len(z)):
        use.append(abs(z[j]-z[j-1]))
    #print(use)
    zz=list(reversed(use))
    if zz==use:
        print("Funny")
    else:
        print("Not Funny")
        
