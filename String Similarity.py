'''t=int(input())
for i in range(0,t):
    s=input()
    use=[]
    ans=len(s)
    for j in range(1,len(s)):
        temp=''
        for k in range(j,len(s)):
            temp+=s[k]
        for k in range(0,len(temp)):
            if temp[k]==s[k] :
                ans+=1
            else:
                break
    print(ans)
'''
t=int(input())
for i in range(0,t):
    s=input()
    z=[]
    z.append(len(s))
    leh=0
    for j in range(1,len(s)):
        ptr=0
        ctr=0
        for k in range(j,len(s)):
            if s[ptr]==s[k]:
                ctr+=1
            else:
                z.append(ctr)
                break
            if k==len(s)-1:
                z.append(ctr)
            ptr+=1
    print(sum(z))
'''
#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    int t ;
    cin >> t;
    string s;
    while(t--){
        cin >> s ;
        ll len = s.size() ;
        int z[len] = {0} ;
        int left = 0 , right =  0 ;
        for(int i = 1 ; i < len ; i++){
            if(i > right){
                left = right = i;
                while(right < len and (s[right] == s[right - left]))
                    right++;
                z[i] = right-left;
                right--;
            } else {
                int k = i - left; // do a mistake here.
                if(z[k] < (right-i+1)){
                    z[i] = z[k];
                } else {
                    left = i;
                    while(right < len and (s[right] == s[right-left]))
                        right++;
                    z[i] = right-left;
                    right--;
                }
            }
        }
        cout << accumulate(z,z+len,len) << endl;
    }
}'''
