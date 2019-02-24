'''n=int(input())
arr=list(map(int,input().split()))
q=int(input())'''
'''for i in range(0,q):
    l,r=map(int,input().split())
    ctr=0
    for j in range(l-1,r):
        before=''
        after=''
        if l-1==j:
            before+='0'
        else:
            for k in range(l-1,j):
                before+=str(arr[k])
        if r-1==j:
            after+='0'
        else:
            for k in range(j+1,r):
                after+=str(arr[k])
        print(before,after)
        ans=int(before)+int(after)
        if ans%30==0:
            ctr+=1
    print(ctr)'''   
'''store=[]
for i in range(0,n):
    before=''
    after=''
    if i==0:
        before+='0'
    else:
        for j in range(0,i):
            before+=str(arr[j])
    if i==len(arr)-1:
        after+='0'
    else:
        for j in range(i+1,n):
            after+=str(arr[j])
    after=int(after)
    before=int(before)
    if (after+before)%30==0:
        store.append(i+1)
#print(store)
for i in range(0,q):
    show=0
    l,r=map(int,input().split())
    for j in range(l,r+1):
        if j in store:
            show+=1
    print(show)'''
length=int(input())
data=list(map(int,input().split()))
fsum=sum(data)
lucky=[]
if(length==1):
    lucky.append(1)
else:
    for i in range(length):
        if i == 0:
            lucky.append(0)
        else:
            lucky.append(lucky[i-1])
        if ((fsum-data[i])%3==0):
            if i==0:
                if(data[length-1]==0):
                    lucky[i]+=1
            elif i==length-1:
                if(data[length-2]==0):
                    lucky[i]+=1
            else:
                if((data[i-1]+data[length-1])%10==0):
                    lucky[i]+=1
lucky.insert(0,0)
#print(lucky)
query=int(input())
for aaa in range(query):
    l,r=list(map(int,input().split()))
    print(lucky[r]-lucky[l-1])
        
