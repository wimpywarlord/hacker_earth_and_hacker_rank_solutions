n=int(input())
s=input()
flagnum=0
flaglower=0
flagupper=0
flagsp=0
num = "0123456789"
lower= "abcdefghijklmnopqrstuvwxyz"
upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sp= "!@#$%^&*()-+"
for i in range(0,len(s)):
    if s[i] in num:
        flagnum=1
    if s[i] in lower:
        flaglower=1
    if s[i] in upper:
        flagupper=1
    if s[i] in sp:
        flagsp=1
ans=0
if flagnum!=1:
    ans+=1
if flaglower!=1:
    ans+=1
if flagupper!=1:
    ans+=1
if flagsp!=1:
    ans+=1
if len(s)+ans<6:
    z=6-(len(s)+ans)
    print(ans+z)
else:
    print(ans)

