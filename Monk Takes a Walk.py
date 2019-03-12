v=[ 'A', 'E', 'I', 'O', 'U' ,'a','e','i','o','u']
for i in range(int(input())):
    ans=0
    s=input()
    for j in s:
        if j in v:
            ans+=1
    print(ans)
            
    
