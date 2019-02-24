a=int(input())
b=int(input())
ctr=0
for j in range(a,b+1):
    use=str(j*j)
    firsthalf='0'
    secondhalf='0'
    for k in range(0,len(use)//2):
       firsthalf+=use[k]
    for k in range(len(use)//2,len(use)):
       secondhalf+=use[k]
    #print(firsthalf)
    #print(secondhalf)
    fh=int(firsthalf)
    sh=int(secondhalf)
    if fh+sh==j :
        print(j,end=' ')
        ctr+=1
if ctr==0:
    print("INVALID RANGE")
        
