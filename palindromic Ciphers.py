t=int(input())
flag=0
for i in range(0,t):
    a=input()
    rev=a[::-1]
    if rev==a:
        print("Palindrome")
    elif flag==1:
        prod=1
        for l in range(0,len(a)):
            prod=prod*(ord(a[l])- 96)
        print(prod)











                
                
            
