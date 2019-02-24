#include <iostream>
#define ll long long
using namespace std;

int main()
{
int n;
cin>>n;
ll x,y,p,dist;
cin>>x>>y>>p;

int arr[n][n];

for(int i = 0;i<n;i++)
{
for(int j = 0;j<n;j++)
{
dist = max(abs(x-i),abs(y-j));
if(dist>=p)
arr[i][j]=0;
else
arr[i][j] = p - dist;
cout<<arr[i][j]<<" ";
}
cout<<endl;
}

return 0;
}
