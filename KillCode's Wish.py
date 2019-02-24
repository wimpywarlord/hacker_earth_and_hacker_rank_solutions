t=int(input())
for i in range(0,t):
    x=input()
    n,m=x.split()
    n=int(n)
    m=int(m)
    z=input()
    l=z.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    print(l)
'''#include <stdlib.h>
#include<stdio.h>
int main()
{
int t,i,j,k,n,m;
scanf("%d",&t);
while(t--)
{
scanf("%d%d",&n,&m);
int a[n];
for(i=0;i<n;i++) scanf("%d",&a[i]);
int count=0;
while(1)
{ 
k=0;
for(i=0;i<n;i++)
{
if(a[i]<=m && a[i]!=0)
{
a[i]=0;
count++;
j=i;
} 
if(a[i]>m)
{
a[i]=a[i]-m;
k++;
} 
}
if(k==0) break;
}
printf("%d\n",j+1);
}
return 0;
}'''
