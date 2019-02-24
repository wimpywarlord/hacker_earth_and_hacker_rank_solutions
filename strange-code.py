'''n=int(input())
ctr=0
time=0
flag=0
while True:
    use=3*(2**ctr)
    for i in range(use,0,-1):
        #print(i)
        ans=i
        time+=1
        if time==n:
            print(ans)
            flag=1
            break
    if flag==1:
        break
    ctr+=1'''
rem = 3
t=int(input())
while t > rem:
    t = t-rem
    rem *= 2

print(rem-t+1)
