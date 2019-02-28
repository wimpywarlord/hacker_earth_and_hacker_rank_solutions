
N=int(input())
arr = input().split()
# arrLength = len(arr)
d=dict()
arr2=[]
for a in arr:
	if a in d.keys():
		d[a] = d[a]+1
	else:
		d[a]=1
		arr2.append(a)
 
Q=int(input())
dlookup = dict()
 
maxKey=max(d,key=d.get)	
maxFrequency = d[maxKey]
 
for x in range(0,Q):
	inp = input()
	query = inp.split()
	f = int(query[1])
	
	
	# if(d[arr[len(arr)-1]] < f):
		# print('0')
		# continue
	
	if(inp in dlookup.keys()):
		print(dlookup[inp])
		continue
	
	#I don't really need arrlength at all. Maxfrequency has got it covered.
	
	# if (f > arrLength):
		# print('0')
		# dlookup[inp]='0'
		# continue
	
	
	# maxKey=max(d,key=d.get)	
	if(maxFrequency < f):
		print('0')
		dlookup[inp] = '0'
		continue
	
	
	if (query[0] == '0'):
		#Type 0 Query
		#First element whose frequency is atleast f	
		flag = 0
		for a in arr2:
			if(d[a] >= f):
				print(a)
				dlookup[inp]= a
				flag = 1 
				break
		if(flag==0):
			print('0')
	else:
		flag = 0
		for a in arr2:
			if(d[a] == f):
				print(a)
				dlookup[inp] = a
				flag = 1
				break
		if(flag == 0):
			print('0')
			
			
################# Previous Code ###############
#### The Code below worked for half the test cases, but showed TLE for others #########
 
# from collections import OrderedDict as ODict
 
# N=int(input())
# arr = input().split()
# d=dict()
# for a in arr:
	# if a in d.keys():
		# d[a] = d[a]+1
	# else:
		# d[a]=1
##print(d)
# dd = ODict()
 
# for a in d.keys():
	# dd[a] = d[a]
 
##print (dd)	
 
# Q=int(input())
 
# for x in range(0,Q):
	# query = input().split()
	# f = int(query[1])
	# if (query[0] == '0'):
		##Type 0 Query
		##First element whose frequency is atleast f	
		# flag = 0
		# for a in arr:
			# if(dd[a] >= f):
				# print(a)
				# flag = 1 
				# break
		# if(flag==0):
			# print('0')
	# else:
		# flag = 0
		# for a in arr:
			# if(dd[a] == f):
				# print(a)
				# flag = 1
				# break
		# if(flag == 0):
			# print('0')
#MY FIRST ATTEMPT
'''n=int(input())
arr=list(map(int,input().split()))
from collections import OrderedDict
d1=OrderedDict()
for i in range(0,n):
    d1[arr[i]]=0
for i in range(0,n):
    d1[arr[i]]+=1
#print(d1)
d1val=list(d1.values())
d1key=list(d1.keys())
t=int(input())
for i in range(0,t):
    typ,number=map(int,input().split())
    if typ==0:
        flag=0
        for j in range(0,len(d1val)):
            if d1val[j]>=number:
                print(d1key[j])
                flag=1
                break
        if flag==0:
            print(0)
    if typ==1:
        flag=0
        for j in range(0,len(d1val)):
             if d1val[j]==number:
                print(d1key[j])
                flag=1
                break
        if flag==0:
            print(0)'''
