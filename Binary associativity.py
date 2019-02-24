'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here
n=input()
for x in range(int(n)):
    p=input()
    if(p=="0 1 1 1"):
        print("Yes")
    elif(p=="0 0 0 1"):
        print("Yes")
    elif(p=="0 1 1 0"):
        print("Yes")
    elif(p=="1 0 0 1"):
        print("Yes")
    elif(p=="0 1 0 1"):
        print("Yes")
    elif(p=="1 1 1 1"):
        print("Yes")
    elif(p=="0 0 0 0"):
        print("Yes")
    elif(p=="0 0 1 1"):
        print("Yes")
    else:
        print("No")
Language: Python 3
