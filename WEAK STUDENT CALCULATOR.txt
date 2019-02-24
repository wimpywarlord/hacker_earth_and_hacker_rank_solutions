n=int(input("ENTRE THE NUMBER OF STUDENTS :"))
a=[]
for i in range(0,n+1):
  if i==n :
    a.append([])
    for j in range(0,6):
        a[i].append(0)
  else:
    a.append([])
    a[i].append(input("REGISTRATION NO:"))
    a[i].append(int(input("PAT 1 MARKS :")))
    a[i].append(int(input("PAT 2 MARKS :")))
    a[i].append(int(input("PAT 3 MARKS :")))
    a[i].append(int(input("PAT 4 MARKS :")))
    a[i].append(0)
    
a[n][0]='avg'

for i in range(0,n+1):
    for j in range(0,6):
        print(a[i][j],end="     ")
    print()
    


for i in range(0,n):
    summ=0
    for j in range(1,5):
        summ=summ+a[i][j]
    avg=summ/4
    a[i][5]=avg
    
print()

for i in range(0,n+1):
    for j in range(0,6):
        print(a[i][j],end="     ")
    print()


classavg=0

for j in range(1,6):
    summ2=0
    for i in range(0,n):
        summ2=summ2+a[i][j]
    classavg=summ2/n
    a[n][j]=classavg

print()

for i in range(0,n+1):
    for j in range(0,6):
        print(a[i][j],end="     ")
    print()



for i in range(0,n):
    counter=0
    for j in range(1,5):
        if a[i][j] < a[i+1][j+1]:
            counter+=1
    if counter >=2:
        print(a[i][0])
            





















        
        
