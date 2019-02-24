t=int(input())
for i in range(0,t):
    nof=int(input())
    xx=input()
    p,w=xx.split()
    p=int(p)
    w=int(w)
    yy=input()
    emp=yy.split()
    for j in range(0,nof-1):
        emp[j]=int(emp[j])
    dfl=[]
    countdfl=0
    empwl=[]
    countempwl=0
    for k in range(0,nof-1):
        dfl.append([])
        empwl.append([])
        zz=input()
        qq=input()
        before1=zz.split()
        before2=qq.split()
        for l in range(0,emp[k]):
            before1[l]=int(before1[l])
            before2[l]=int(before2[l])
            dfl[countdfl].append(before1[l])
            
            empwl[countempwl].append(before2[l])
        countempwl+=1
        countdfl+=1
    print(emp)
    print(dfl)
    print(empwl)
         # INPUT TAKING IS DONE NOW LETS EFFICIENTLY CODE FOR THE PROBLEM.
    sumofp=0
    sumofw=0
    sumofpl=[]
    sumofwl=[]
    for i in range(0,nof-1):
        sumofp+=emp[i]
        for j in range(i,nof-1):
            for k in range(0,len(empwl[j])):
                sumofw+=empwl[j][k]
            break
        for j in range(0,nof-1):
            for k in range(0,len(dfl[j])):
                print(dfl[j][k])
                if dfl[j][k]==i+1:
                    sumofp-=1
                    sumofw-=empwl[j][k]
        sumofwl.append(sumofw)
        sumofpl.append(sumofp)
    print(sumofpl)
    print(sumofwl)



    flag=0
    c=0
    for i in range(0,nof-1):
        c+=1
        if sumofpl[i]>p and sumofwl[i]>w:
            flag=1
            break
            
        
    if flag==0:
        print(nof)
    else:
        print(c+1)

        
        

        
        
