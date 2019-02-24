t=int(input())
for i in range(0,t):
    s1=input()
    s2=input()
    flag=0
    for j in range(0,len(s1)):
        if s1[j] in s2:
            flag=1
    if flag==1:
        print("YES")
    else:
        print("NO")
