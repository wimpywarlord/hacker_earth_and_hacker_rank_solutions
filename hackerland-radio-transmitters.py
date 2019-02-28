'''n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
#print(arr)
maxx=max(arr)
minn=min(arr)
ans=0
ctr=minn
while maxx>=ctr:
    #print(ctr)
    ctr+=2*k+1
    if ctr in arr :
        ans+=1
    else:
        while ctr not in arr and ctr<n:
            ctr+=1
        ans+=1
if ans==0:
    print(1)
else:
    print(ans)'''
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <math.h>
#include <vector>
#define forn(i, a, n) for (int i = a; i < n; i++)
using namespace std;

int ijs(vector<int> arr, int pi, int to_find, int n) {
  int l;
  forn(i, pi, n) {
    if (arr[i] <= to_find) {
      l = i;
    } else
      break;
  }
  return l;
}

int main() {
  int n, k, par = 1;
  cin >> n >> k;
  vector<int> arr(n);
  forn(i, 0, n) cin >> arr[i];
  sort(arr.begin(), arr.end());
  int mid = arr[0] + k;
  int indm, right, p = 0;
  forn(i, 0, n) {
    if (i == n - 1) {
      p++;
      break;
    }
    indm = ijs(arr, i, mid, n);
    i = indm;
    p++;
    right = ijs(arr, i, arr[i] + k, n);
    i = right + 1;
    mid = arr[i] + k;
    i--;
  }
  cout << p;
  return 0;
}



    
    
