t=int(input())
for t in range(0,t):
    n=input()
    ms=0
    for j in range(0,len(n)):
        if n[j]=='0':
            ms+=6
        elif n[j]=='1':
            ms+=2
        elif n[j]=='2':
            ms+=5
        elif n[j]=='3':
            ms+=5
        elif n[j]=='4':
            ms+=4
        elif n[j]=='5':
            ms+=5
        elif n[j]=='6':
            ms+=6
        elif n[j]=='7':
            ms+=3
        elif n[j]=='8':
            ms+=7
        elif n[j]=='9':
            ms+=6
    if ms==3:
        print(7)
    elif ms%2==0:
        use=ms//2
        ans=''
        for j in range(0,use):
            ans+='1'
        ans=int(ans)
        print(ans)
    else :
        use=ms//2
        ans='7'
        for j in range(0,use-1):
            ans+='1'
        ans=int(ans)
        print(ans)
            
