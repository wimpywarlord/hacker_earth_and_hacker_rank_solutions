x=int(input())
b=[]
while x>0:
    y=x%10
    b.insert(0,y)
    x=x//10
print(b)
