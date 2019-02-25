#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    # row 0 = 0, column 0  = 0
    l1 = len(s1)
    l2 = len(s2)
    # we only need history of previous row
    lcs = [[0]*(len(s1)+1) for _ in range(2)]
    #lcs_letters = [['']*(len(s1)+1) for _ in range(2)]
    
    # i in s1 = i+1 in lcs
    for i in range(l1):
        # get index pointers for current and previous row
        li1 = (i+1)%2
        li = i%2
        # j in s1 = j+1 in lcs
        for j in range(l2):
            # i and j are used to step forward in each string.
            # Now check if s1[i] and s2[j] are equal 
            if s1[i] == s2[j]:
                # Now we have found one longer sequence 
                # than what we had previously found.
                # so add 1 to the length of previous longest
                # sequence which we could have found at
                # earliest previous position of each string,
                # therefore subtract -1 from both i and j
                lcs[li1][j+1] = (lcs[li][j] + 1) 
                #lcs_letters[li1][j+1] = lcs_letters[li][j]+s1[li]

            # if not matching pair, then
            # get the biggest previous value
            elif lcs[li1][j] > lcs[li][j+1]:
                lcs[li1][j+1] = lcs[li1][j] 
                #lcs_letters[li1][j+1] = lcs_letters[li1][j]
            else:
                lcs[li1][j+1] = lcs[li][j+1] 
                #lcs_letters[li1][j+1] = lcs_letters[li][j+1]
    #print(lcs_letters[(i+1)%2][j+1])
    return lcs[(i+1)%2][j+1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
