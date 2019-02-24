'''t=int(input())
for i in range(0,t):
    z=input()
    x,y,l,m,a,b=z.split()
    x=int(x)
    y=int(y)
    l=int(l)
    m=int(m)
    a=int(a)
    b=int(b)
    check1=x//2
    check2=y//2
    if a<=check1 and b>=check2:
        print("bottom-right")
    elif a>check1 and b>=check2:
        print("bottom-left")
    elif a<=check1 and b<check2:
        print("top-right")
    elif a>check1 and b<check2:
        print("top-left")
'''
def main():
	T=int(input())
	
	for case in range(0,T):
		inp = input().split(' ')
		
		x = int(inp[0])
		y = int(inp[1])
		l = int(inp[2])
		m = int(inp[3])
		a = int(inp[4])
		b = int(inp[5])
		
		
		if (x-a)>=l and b>=m:
			print('bottom-right')
		elif a>=l and b>=m:
			print('bottom-left')
		elif (x-a)>=l and (y-b)>=m:
			print('top-right')
		else:
			print('top-left')
			
		    
 
 
main()
