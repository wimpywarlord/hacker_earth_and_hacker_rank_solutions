t=int(input())
for i in range(0,t):
    z=list(map(int,input().split()))
    temp1=z[0]
    temp2=z[1]
    #print(temp1)
    #print(temp2)
    for i in range(2,z[2]+1):
        temp3=temp2+2*temp1
        #print(temp3,end=' ')
        temp1=temp2
        temp2=temp3
    print(temp2%(10**9+9))
