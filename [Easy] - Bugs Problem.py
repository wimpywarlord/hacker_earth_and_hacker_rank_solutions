t=int(input())
mat=[]
import math
for i in range(0,t):
    z=list(map(int,input().split()))
    x=list(map(int,input().split()))
    totalways=((math.factorial(z[0]+z[1]))//(math.factorial(z[0])*math.factorial(z[1])))
    print(totalways)
    minus=totalways=((math.factorial(x[0]+x[1]))//(math.factorial(x[0])*math.factorial(x[1])))
    print(minus)
                                           
