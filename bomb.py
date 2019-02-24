t=int(input())
for i in range(0,t):
    b=input()
    x=[]
    for k in b:
        x.append(k)
    for j in range (0,len(x)):
      if j-2>=0 and j+2<len(x):
        if x[j]=='W' and (x[j+2]=='B' or  x[j+1]=='B' or x[j-2]=='B' or x[j-1]=='B'):
                x[j]='0'
      elif j-2==-2 :
        if x[j]=='W' and (x[j+2]=='B' or  x[j+1]=='B'):
                x[j]='0'
                      
      elif j+2==len(x)+ 1:
        if x[j]=='W' and (x[j-2]=='B' or x[j-1]=='B'):
                x[j]='0'
      elif j-2==-1 :
        if x[j]=='W' and (x[j+2]=='B' or  x[j+1]=='B' or x[j-1]=='B'):
                x[j]='0'
         
      elif j+2==len(x) :
        if x[j]=='W' and (x[j-2]=='B' or x[j - 1]=='B' or x[j+1]=='B'):
                x[j]='0'
    print(x)
    counter=0
    for m in x:
        if m=='0':
             counter+=1
    print(counter)
