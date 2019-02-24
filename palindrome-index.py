"""t=int(input())
for i in range(0,t):
    s=input()
    srev=s[::-1]
    #print(s)
    #print(srev)
    if s==srev:
        print(-1)
    else:
        s=list(s)
        #print(s)
        #print(srev)
        for j in range(0,len(s)//2):
            x=s[j]
            s.pop(j)
            #print(s)
            srev=s[::-1]
            #print(srev)
            if s==srev:
                print(j)
                break
            else:
                s.insert(j,x)
            #print()"""
def find_mismatching_pair(s):
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return i, j
    
    
def is_palindrome(s):
    i, j = find_mismatching_pair(s)
    return True if j <= i else False
    
    
def correct(s):
    i, j = find_mismatching_pair(s)
    return -1 if j <= i else i if is_palindrome(s[i+1 : j+1]) else j


for _ in range(int(input())):
    print(correct(input()))
                
