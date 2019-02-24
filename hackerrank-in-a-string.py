t=int(input())
for i in range(0,t):
    s=input()
    check=['h','a','c','k','e','r','r','a','n','k']
    newl=[]
    imp=0
    for j in range(0,len(check)):
        for k in range(imp,len(s)):
            if s[k]==check[j]:
                newl.append(s[k])
                imp=k+1
                break
                
    print(newl)
    if newl!=check:
        print("NO")
    else:
        print("YES")
    
            
                
        
