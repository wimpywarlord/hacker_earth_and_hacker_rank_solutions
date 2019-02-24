t=int(input())
for i in range(0,t):
    n=int(input())
    if n==1 or n==2:
        print(-1)
    else:
        ctr1=n
        use1=0
        use2=0
        use3=0
        use4=0
        flag=0
        for j in range(0,n):
            if ctr1%3==0 and j%5==0:
                flag=1
                use1=ctr1
                use2=j
                break
            ctr1-=1
        ctr2=n
        for j in range(0,n):
            if ctr2%5==0 and j%3==0:
                flag=1
                use3=ctr2
                use4=j
                break
            ctr2-=1
        if flag==0:
            print(-1)
        else:
            if use1==0 and use2==0:
                ans=''
                for j in range(0,use3):
                    ans+='3'
                for j in range(0,use4):
                    ans+='5'
                print(ans)
            else:
                ans=''
                for j in range(0,use1):
                    ans+='5'
                for j in range(0,use2):
                    ans+='3'
                print(ans)
            
                
            
        
