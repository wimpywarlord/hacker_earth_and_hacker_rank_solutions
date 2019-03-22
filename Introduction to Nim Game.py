'''#include <bits/stdc++.h>
using namespace std;
int main()
{
    int q;
    cin>>q;
    while(q--)
    {
        int n;
        cin>>n;
        int ans=0;
        int x;
        for(int i=0;i<n;i++)
        {
            cin>>x;
            ans^=x;
        }
        if(ans!=0)
            cout<<"First\n";
        else
            cout<<"Second\n";
    }
}'''
