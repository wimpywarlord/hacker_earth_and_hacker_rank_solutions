"""t=int(input())
for b in range(0,t):
    r=int(input())
    ctr=0
    for i in range(1,r):
        for j in range(1,r-1):
            for k in range(1,r-2):
                if (i+3*j+4*k)==r:
                    ctr+=1
                    print(i,j,k)
    print(ctr)"""

# A naive recursive Python program 
# to find number of non-negative  
# solutions for a given linear equation 
  
# Recursive function that returns  
# count of solutions for given rhs 
# value and coefficients coeff[stat...end] 
def countSol(coeff, start, end, rhs): 
  
    # Base case 
    if (rhs == 0): 
        return 1
  
    # Initialize count of solutions 
    result = 0 
  
    # One by one subtract all smaller or  
    # equal coefficients and recur 
    for i in range(start, end+1): 
        if (coeff[i] <= rhs): 
            result += countSol(coeff, i, end, 
                               rhs - coeff[i]) 
  
    return result 
  
# Driver Code
t=int(input())
for i in range(0,t):
    
    coeff = [1,3,4] 
    rhs = int(input())
    n = len(coeff)
    print(countSol(coeff, 1, n - 1, rhs)) 

