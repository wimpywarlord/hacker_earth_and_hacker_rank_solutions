t=int(input())
use=[]
for i in range(0,t):
    z=list(map(str,input().split()))
    use.append(z)
#print(use)
find=input()
for i in range(0,t):
    if find==use[i][0]:
        print("{:.2f}".format((float(use[i][1])+float(use[i][2])+float(use[i][3]))/3))
        break
