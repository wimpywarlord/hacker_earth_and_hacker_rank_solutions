'''t=int(input())
for i in range(0,t):
    use=list(map(int,input().split()))
    del use[0]
    #print(use)
    arr=list(map(int,input().split()))
    from math import gcd
    lcm = arr[0]
    for j in arr[1:]:
      lcm = lcm*j//gcd(lcm, i)
    flag=0
    print(lcm)
    for j in range(0,len(arr)):
        print(lcm//arr[j],use[0])
        print(lcm//arr[j],use[0])
        print(lcm//arr[j],use[0])
        if (lcm//arr[j])%use[0]!=0 and (lcm//arr[j])%use[1]!=0 and (lcm//arr[j])%use[2]!=0:
            flag=1
    if flag==1:
        print("She can't")
    else:
        print("She can")'''
'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here
t=int(input())
for i in range(0,t):
    r1=input().split()
    n=int(r1[0])
    r1=r1[1:]
    r=list(map(int,r1))
    a=list(map(int,input().split()))
    m=min(a)
    for j in a:
        if(j!=m):
            u=j/m
            if(u%r[0]!=0 and u%r[1]!=0 and u%r[2]!=0):
                print("She can't")
                break
    else:
        print("She can")
Language: Python 3
    
    
    
