'''t=int(input())
l=[]
for i in range(0,t):
    z=input()
    a=z.split("-")
    l.append(a)
print(l)
flag=0
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        for k in range(0,len(l)):
            for m in range(0,len(l[k])):
                if i!=k and l[i][1][0]==l[k][0][0] and l[i][1][1]==l[k][0][1] and  (l[i][1][3]>l[k][0][3] or (l[i][1][3]>=l[k][0][3] and l[i][1][4]>l[k][0][4])):
                    flag=1
                if i!=k and l[i][1][0]<l[k][1][0] and l[i][1][1]<l[k][1][1] and l[i][0][0]>l[k][0][0] or  l[i][0][1]>l[k][0][1]:
                    flag=1
if flag==1:
    print("Will need a moderator!")
else:
    print("Who needs a moderator?")'''
#define TRUE 1
#define FALSE !TRUE
int main() {
int n;
int day[1440]={0};
int hh1,mm1,hh2,mm2;
int start,end;
int needsModerator=FALSE;

scanf("%d",&n);
while(n--) {
scanf("%d:%d-%d:%d",&hh1,&mm1,&hh2,&mm2);
start=hh1*60+mm1;
end=hh2*60+mm2;

for(int i=start; i<end; i++) {
day[i]++;
if (day[i]>=2) {
needsModerator=TRUE;
break;
}
}
}
printf("%s",needsModerator?"Will need a moderator!":"Who needs a moderator?");
return 0;
}
