t=int(input())
for i in range(0,t):
    q=input()
    s=list(q)
    p1=0
    p2=0
    u=0
    flag=0
    for j in range(0,len(s)):    
       if u%2==0:
         while s[j] in s:
           s.remove(s[j])
       elif u%2==1: 
         while s[j] in s:
           s.remove(s[j])
       u+=1
    print(s)
    print(u)
    if u % 2==0:
        print("Player2")
    else:
        print("Player1")

    
