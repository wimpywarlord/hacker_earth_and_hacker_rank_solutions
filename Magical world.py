97, 101, 103, 107, 109, 113, 127, 131, 137, 139
t=int(input())
for i in range(0,t):
    l=int(input())
    s=input()
    ss=[]
    for j in range(0,len(s)):
        ss.append(s[j])
    for j in range(0,len(ss)):
        x=ord(ss[j])
        if x==65 or x==66 or x==68 or x==69:
            ss[j]=chr(67)
        elif x==70 or x==72 :
            ss[j]=chr(71)
        elif x==74 or x==75 or x==76:
            ss[j]=chr(73)
        elif x==77 or x==78 or x==80 or x==81 :
            ss[j]=chr(79)
        elif x==82 or x==84 or x==85 or x==86:
            ss[j]=chr(83)
        elif x==87 or x==88 or x==90:
            ss[j]=chr(89)
        elif x==98 or x==99:
            ss[j]=chr(97)
        elif x==100 or x==102:
            ss[j]=chr(101)
        elif x==104 or x==105:
            ss[j]=chr(103)
        elif x==106 or x==108:
            ss[j]=chr(107)
        elif x==110 or x==111 :
            ss[j]=chr(109)
        elif x==112 or x>113:
            ss[j]=chr(113)
    
    #print(ss)
    ans="".join(ss)
    print(ans)
        
    
