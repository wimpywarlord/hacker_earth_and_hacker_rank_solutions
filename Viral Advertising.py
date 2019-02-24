import math
def main():
    n=int(input())
    for i in range(0,n):
        if i==0:
            v=5
            like=math.floor(5//2)
        else:
            v=math.floor(v//2)*3
            like+=math.floor(v//2)
    print(like)        
main()
