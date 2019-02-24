#BRUTE FORCE IS NOT WORKING
# THEORY :
import math   
one = [[0 for x in range(32)]  
      for y in range(100001)]  
MAX = 2147483647
def make_prefix(A, n) : 
    global one, MAX 
    for j in range(0 , 32) : 
        one[0][j] = 0
    for i in range(1, n+1) :  
        a = A[i - 1] 
        for j in range(0 , 32) : 
            x = int(math.pow(2, j))
            if (a & x) : 
                one[i][j] = 1 + one[i - 1][j] 
            else : 
                one[i][j] = one[i - 1][j]           
def Solve(L, R) :  
    global one, MAX
    l = L  
    r = R 
    tot_bits = r - l + 1
    X = MAX
    for i in range(0, 31) :  
        x = one[r][i] - one[l - 1][i] 
        if (x >= (tot_bits - x)) :     
            ith_bit = pow(2, i) 
            X = X ^ ith_bit 
    return X 
n,q= map(int,input().split())
A = list(map(int,input().split()))
L=[]
R=[]
for j in range(0,q):
    z=list(map(int,input().split()))
    L.append(z[0])
    R.append(z[1])

make_prefix(A, n) 
for j in range(0, q) : 
    print (Solve(L[j], R[j]),end="\n") 
