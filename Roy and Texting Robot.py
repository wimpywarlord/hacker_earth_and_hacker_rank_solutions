t=int(input())
for i in range(0,t):
    s=input()
    '''if s[0]=='.' or s[0]==',' or s[0]=='?' or s[0]=='!' or s[0]=='1':
            ptr=1
    if s[0]=='a' or s[0]=='b' or s[0]=='c' or s[0]=='2':
            ptr=2
    if s[0]=='d' or s[0]=='e' or s[0]=='f' or s[0]=='3':
            ptr=3
    if s[0]=='g' or s[0]=='h' or s[0]=='i' or s[0]=='4':
            ptr=4
    if s[0]=='j' or s[0]=='k' or s[0]=='l' or s[0]=='5':
            ptr=5
    if s[0]=='m' or s[0]=='n' or s[0]=='o' or s[0]=='6':
            ptr=6
    if s[0]=='p' or s[0]=='q' or s[0]=='r'  or s[0]=='s' or s[0]=='7':
            ptr=7
    if s[0]=='t' or s[0]=='u' or s[0]=='v' or s[0]=='8':
            ptr=8
    if s[0]=='w' or s[0]=='x' or s[0]=='y' or s[0]=='z' or s[0]=='9':
            ptr=9 
    if s[0]=='0' or s[0]=='_' :
            ptr=0'''
    ptr=1    
    ctr=0
    for j in range(0,len(s)):
        if s[j]=='.' or s[j]==',' or s[j]=='?' or s[j]=='!' or s[j]=='1':
            #print("!")
            if ptr!=1:
                #print("!!")
                ctr+=1
            if s[j]=='.':
                ctr+=1
            if s[j]==',':
                ctr+=2
            if s[j]=='?':
                #print(345)
                ctr+=3
            if s[j]=='!':
                ctr+=4
            if s[j]=='1':
                ctr+=5
            ptr=1
        if s[j]=='a' or s[j]=='b' or s[j]=='c' or s[j]=='2':
            #print("@")
            if ptr!=2:
                #print("@@")
                ctr+=1
            ptr=2
            if s[j]=='a':
                ctr+=1
            if s[j]=='b':
                ctr+=2
            if s[j]=='c':
                ctr+=3
            if s[j]=='2':
                ctr+=4
            
        if s[j]=='d' or s[j]=='e' or s[j]=='f' or s[j]=='3':
            #print("#")
            if ptr!=3:
                #print("##")
                ctr+=1
            
            ptr=3
            if s[j]=='d':
                ctr+=1
            if s[j]=='e':
                ctr+=2
            if s[j]=='f':
                ctr+=3
            if s[j]=='3':
                ctr+=4     
        if s[j]=='g' or s[j]=='h' or s[j]=='i' or s[j]=='4':
            #print("$")
            if ptr!=4:
                #print("$$")
                ctr+=1
            if s[j]=='g':
                ctr+=1
            if s[j]=='h':
                ctr+=2
            if s[j]=='i':
                #print(678)
                ctr+=3
            if s[j]=='4':
                ctr+=4
            ptr=4
        if s[j]=='j' or s[j]=='k' or s[j]=='l' or s[j]=='5':
            #print("%")
            if ptr!=5:
                #print("%%")
                ctr+=1
            ptr=5
            if s[j]=='j':
                ctr+=1
            if s[j]=='k':
                ctr+=2
            if s[j]=='l':
                ctr+=3
            if s[j]=='5':
                ctr+=4
        if s[j]=='m' or s[j]=='n' or s[j]=='o' or s[j]=='6':
            #print("^")
            if ptr!=6:
                #print("^^")
                ctr+=1
            ptr=6
            if s[j]=='m':
                ctr+=1
            if s[j]=='n':
                ctr+=2
            if s[j]=='o':
                ctr+=3
            if s[j]=='6':
                ctr+=4

        if s[j]=='p' or s[j]=='q' or s[j]=='r'  or s[j]=='s' or s[j]=='7':
            #print("&")
            if ptr!=7:
                #print("&&")
                ctr+=1
            ptr=7
            if s[j]=='p':
                ctr+=1
            if s[j]=='q':
                ctr+=2
            if s[j]=='r':
                ctr+=3
            if s[j]=='s':
                ctr+=4
            if s[j]=='7':
                ctr+=5
        if s[j]=='t' or s[j]=='u' or s[j]=='v' or s[j]=='8':
            #print("*")
            if ptr!=8:
                #print("**")
                ctr+=1
            ptr=8
            if s[j]=='t':
                ctr+=1
            if s[j]=='u':
                #print(123)
                ctr+=2
            if s[j]=='v':
                ctr+=3
            if s[j]=='8':
                ctr+=4
        if s[j]=='w' or s[j]=='x' or s[j]=='y' or s[j]=='z' or s[j]=='9':
            #print("(")
            if ptr!=9:
                #print("((")
                ctr+=1
            ptr=9
            if s[j]=='w':
                ctr+=1
            if s[j]=='x':
                ctr+=2
            if s[j]=='y':
                ctr+=3
            if s[j]=='z':
                ctr+=4
            if s[j]=='9':
                ctr+=5
        if s[j]=='0' or s[j]=='_' :
            #print(")")
            if ptr!=0:
                #print("))")
                ctr+=1
            ptr=0
            if s[j]=='0':
                ctr+=2
            if s[j]=='_':
                #print(234)
                ctr+=1
    print(ctr)
            
