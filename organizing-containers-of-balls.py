'''
1. Swaps that happen between any 2 buckets are always of equal value (you can exchange 1 for 1 but not 2 for 1, ratio should always be 1:1), therefore the number of balls in each bucket will always remain the same. 

2. We need to make sure that the total number of balls in each container should equal the number of balls of any type 't' for a fair trade(1:1 ratio). This is done to check whether there are any type 't' balls that satisfy the requirements of the solution (i.e. we want all balls of a single type 't' in only one container).

3. Calculate the number of balls in each container(sum of rows) and store it in a list.

4. Calculate the number of balls of each type(sum of columns) and store it in a list.

5. Sort the two lists and compare them. If they are equal then a solution exists otherwise, no solution exists.

Try theses cases to see and understand the pattern:

Possible:

2
1 0
0 1

2
1 2
2 1

3
0 4 0
2 0 1
1 0 2

4
1 2 3 4
2 1 4 3
3 4 2 1
4 3 1 2

4
0 0 5 0
4 0 0 0
0 2 0 1
0 1 0 2

Impossible:

2
2 1
0 0

2
2 1
0 1

3
1 2 3
3 2 1
2 3 1

3
1 0 0
0 2 0
0 2 0

4
1 2 1 3
2 1 3 1
1 3 2 1
3 2 1 1

Note: For more test cases try Solved Sudoku puzzles.

Here is Python2 Solution:

'''

q = int(raw_input().strip())

for x in xrange(q):
    
    n = int(raw_input().strip())
    m = []
    rowsum = [0]*n
    colsum = [0]*n
    
    for i in xrange(n):
        m.append(map(int,raw_input().strip().split(' ')))
        rowsum[i] = sum(m[-1])
        colsum = map(lambda a, b: a+b, colsum, m[-1])
        
    rowsum.sort()
    colsum.sort()
    
    if rowsum == colsum:
        print ('Possible')
    else:
        print )

