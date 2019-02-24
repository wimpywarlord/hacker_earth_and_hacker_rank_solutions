s=input()
count=0
for i in range(0,len(s)):
  if i!=len(s)-1:
    if s[i]=='r' and s[i+1]=='r' :
        count+=1
print(count)
