t=int(input())
months=['January','February','March','April','May','June','July','August','September','October','November','December']
for i in range(0,t):
    x=input()
    date=x.split()
    counter=0
    for j in range(0,len(months)):
         if months[j]==date[1]:
              counter=j+1
    if date[0]=='1' and date[1]=='January' :
         print("31 December ",int(date[2])-1)
    elif date[0]=='1' and date[1]=='March' and int(date[2])%4==0:
         print("29 February ",date[2])
    elif date[0]=='1' and date[1]=='March' and int(date[2])%4!=0:
         print("28 February ",date[2])
    elif date[0]=='1' and date[1]=='August':
         print("31 July ",date[2])
    elif date[0]=='1' and date[1]=='September':
         print("31 August ",date[2])
    elif date[0]=='1' and date[1]=='October':
         print("31 September ",date[2])
    elif date[0]=='1' and date[1]=='November':
         print("31 October ",date[2])
    elif date[0]=='1' and date[1]=='December':
         print("31 November ",date[2])
    elif date[0]=='1'  and counter%2==0:
         for j in range(0,len(months)):
              if months[j]==date[1]:
                    date[1]=months[j-1]
         date[0]='31'
         s=" ".join(date)
         print(s)
    elif date[0]=='1'  and counter%2==1 :
         for j in range(0,len(months)):
              if months[j]==date[1]:
                    date[1]=months[j-1]
         date[0]='30'
         s="".join(date)
         print(s)
    else:
        date[0]=int(date[0])- 1
        s="".join(date)
        print(s)
         
