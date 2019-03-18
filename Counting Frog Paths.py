x, y, s, t = ( int(i) for i in input().split() )
 
j, c = t, 0
 
for i in range (0, t+1):
    if(j >= y and j <= y+s):
        c += min (max(0,i-x+1),s+1)
    j -= 1
    
print(c)
