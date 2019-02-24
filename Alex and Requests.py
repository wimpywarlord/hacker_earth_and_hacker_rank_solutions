n=int(input())
comp=[]
for i in range(0,n):
    comp.append(0)
print(comp)
q=int(input())
for i in range(0,q):
    p=int(input())
    flag=0
    print(p)
    for j in range(0,len(comp)):
        if p>comp[j]:
            comp[j]=p
a"""n=int(input())
comp=[]
for i in range(0,n):
    comp.append(0)
#print(comp)
q=int(input())
for i in range(0,q):
    p=int(input())
    flag=0
    for j in range(0,len(comp)):
        if p>comp[j] :
            comp[j]=p
            flag=1
            print("YES")
            break
    if flag==0:
        print("NO")"""
            # MISSED THE CONDITION At any instance, ith 
            #system can process only one request with priority i or above.
sys=[]
noSys=int(input())
for i in range(noSys):
    sys.append(0)
noReq=int(input())
for i in range(noReq):
    flag=0
    pri=int(input())
    for i in range(noSys,0,-1):
        if pri>sys[i-1] and pri>=i:
            sys[i-1]=pri
            print("YES")
            flag=1
            break
    if flag!=1:
        print("NO")
        
    
        
        
            flag=1
            print(i+1,"->","YES")
            break
    if flag==0:
        print(i+1,"->","NO")
    print(comp)
    
        
        
