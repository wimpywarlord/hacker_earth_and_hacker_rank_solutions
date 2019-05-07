n,q=map(int,input().split())
arr=list(map(int,input().split()))
#print(arr)
for i in range(0,q):
    x=input()
    if x[0]=="1":
        #print(arr[int(x[2])-1])
        if  arr[int(x[2])-1]==1:
            #print("^")
            arr[int(x[2])-1]=0
        if  arr[int(x[2])-1]==0:
            #print("#")
            arr[int(x[2])-1]=1
    #print(arr)
    if x[0]=="0":
        t=int(x[4])
        #print(arr[t-1])
        if arr[t-1]==0:
            print("EVEN")
        else:
            print("ODD")
            
        

N, Q = input().split()
 
data = input().split()
 
for i in range(int(Q)):
	query = input().split()
	if query[0] == '1':
		index = int(query[1]) - 1
		if data[index] == '0':
			data[index] = '1'
		else:
			data[index] = '0'
	else:
		indexR = int(query[2]) - 1
		if data[indexR] == '0':
			print('EVEN')
		else:
			print('ODD')
