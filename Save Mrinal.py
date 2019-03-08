'''n=int(input())
arr=list(map(int,input().split()))
q=int(input())
for i in range(q):
    l=list(map(int,input().split()))
    d={}
    if len(l)==1:
        print(0)
    else:
        for j in range(l[0]-1,l[1]):
            d[arr[j]]=0
        if not d:
            print(0)
        else:
            print(len(d))
 '''       
'''
hThe syntax of extend() method is:

list1.extend(list2)
Here, the elements of list2 are added to the end of list1.

extend() Parameters
As mentioned, the extend() method takes a single argument (a list) and adds it to the end.

If you need to add elements of other native datatypes (like tuple and set) to the list, you can simply use:

# add elements of a tuple to list
list.extend(list(tuple_type))
or even easier

list.extend(tuple_type)
'''
n=int(input())
arr=[int(x) for x in input().split()]
q=int(input())
temp=[]
i=0
while i != q:
    qq=[int(x) for x in input().split()]
    temp.extend(qq)
    if len(temp)>= 2:
        l=temp.pop(0)
        r=temp.pop(0)
        subarr=arr[l-1:r]
        length=len(set(subarr))
        print(length)
        i=i+1
    else:
        pass
