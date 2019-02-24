a=input()
num=0
for i in a:
    x=ord(i)
    num=num*10 + (x - 96)
print(num)
if num%6==0:
    print("YES")
else :
    print("NO")
