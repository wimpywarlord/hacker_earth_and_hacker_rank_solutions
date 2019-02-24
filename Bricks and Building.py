n=int(input())
h=[]
for i in range(0,n):
    s=int(input())
    h.append(s)
q=int(input())
b=[]
for j in range(0,q):
    k=int(input())
    b.append(k)
for i in range(0,len(b)):
    ctr=0
    for j in range(0,len(h)):
        else:
            if h[j]%b[i]==0:
                ctr+=1
    print(ctr)
'''
#include<bits/stdc++.h>
using namespace std;
int main()
{
int n,h[100001]={0};
cin>>n;
int y;
for(int i=0;i<n;i++)
{
cin>>y;
for(int j=1;j<=sqrt(y);j++)
{
if (y%j == 0)
{

if (y/j == j)
h[j]++;

else 
{
h[j]++;
h[y/j]++;
}
}
}
}
int q;
cin>>q;
while(q--)
{
int d;
cin>>d;

cout<<h[d]<<endl;
}
}
'''
