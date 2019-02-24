t=int(input())
for i in range(0,t):
    n=int(input())
    s1=input()
    #print(s1)
    s2=input()
    #print(s2)
    flag=0
    for j in range(0,len(s1)):
        for k in range(j,len(s2)):
            if s1[j] != s2[k] :
                ctr2+=1
            break
    #print(ctr)
    #print(ctr2)
    if ctr2>2:
        print("NO")
    else:
        print("YES")
'''
'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here
t = int(input())
for j in range(t):
    n = int(input())
    a = input()
    b = input()
    count = 0;
    c = []
    for i in range(n):
        if a[i] != b[i]:
            count += 1
            c.append(i)
    if count > 3:
        print("NO")
    elif count < 2:
        print("YES")
    elif count == 2:
        if a[c[0]] == a[c[1]] or b[c[0]] == b[c[1]]:
            print("YES")
        elif a[c[0]] == b[c[1]] or b[c[0]] == a[c[1]]:
            print("YES")
        else:
            print("NO")
    elif count == 3:
        if a[c[0]] == a[c[1]] and b[c[0]] == b[c[1]]:
            print("YES")
        elif a[c[0]] == b[c[1]] and b[c[0]] == a[c[1]]:
            print("YES")
        elif a[c[1]] == a[c[2]] and b[c[1]] == b[c[2]]:
            print("YES")
        elif a[c[0]] == a[c[2]] and b[c[0]] == b[c[2]]:
            print("YES")
        elif a[c[1]] == b[c[2]] and b[c[1]] == a[c[2]]:
            print("YES")
        elif a[c[0]] == b[c[2]] and b[c[0]] == a[c[2]]:
            print("YES")
        else:
            print("NO")
            '''
    
