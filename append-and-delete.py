'''s1=input()
s2=input()
empty=''
n=int(input())
if len(s1)>len(s2):
    for j in range(0,len(s2)):
        temp=empty+s2[j]
        if temp in s1:
            empty+=s2[j]
        else:
            break
    #print(empty)
    z=len(s1)-(2*len(empty))+len(s2)
    if z>n:
        print("No")
    else:
        print("Yes")
else:
    for j in range(0,len(s1)):
        temp=empty+s1[j]
        if  temp in s2:
            empty+=s1[j]
        else:
            break
    #print(empty)
    z=len(s1)-(2*len(empty))+len(s2)
    if z>n:
        print("No")
    else:
        print("Yes")'''

s = input().strip()
t = input().strip()
k = int(input().strip())

numSameChars = min(len(s), len(t))
for i in range(len(t)):
    if s[:i] != t[:i]:
        numSameChars = i-1
        break

diff = len(s)-numSameChars + len(t)-numSameChars
print('Yes' if (diff <= k and diff%2 == k%2) or len(s) + len(t) < k else 'No')
