n=int(input())
s=list(map(int,input().split()))
ctr=0
copy=sorted(s)
l=[]
for i in range(0,len(s)):
    if i!=len(s)-1 :
        if s[i]>s[i+1]:
            ctr+=1
            #print(s[i])
            l.append(i)
#print(ctr)
if ctr>2:
    
    b=list(s)
    #print(copy)
    flag=0
    bigflag=0
    for i in range(0,len(s)):
        for j in range(0,len(s)-i):
            use=[]
            pos=0
            for k in range(i,len(s)-j):
                use.append(s[k])
                pos=k
            #print(use,"*")
            ptr=0
            use.reverse()
            for k in range(i,len(b)-j):
                b[k]=use[ptr]
                ptr+=1
            #print(b,"&")
            if b==copy:
                flag=1
                print("yes")
                print("reverse",i+1,pos+1)
                bigflag=1
                break
            b=list(s)
        if bigflag==1:
            break
            
    if flag==0:
        print("no")
else:
    if len(s)==2:
        temp=s[0]
        s[0]=s[1]
        s[1]=temp
        if s==copy:
            print("yes")
            print("swap",1,2)
    else:   
        #print(l[0])
        #print(l[1])
        if len(l)==1:
            temp=s[l[0]]
            s[l[0]]=s[l[0]+1]
            s[l[0]+1]=temp
            #print(s)
            if s==copy:
                print("yes")
                print("swap",l[0]+1,l[0]+2)
            else:
                print("no")
        else:
            temp=s[l[0]]
            s[l[0]]=s[l[1]+1]
            s[l[1]+1]=temp
            #print(s)
            if s==copy:
                print("yes")
                print("swap",l[0]+1,l[1]+2)
            else:
                print("no")
                
