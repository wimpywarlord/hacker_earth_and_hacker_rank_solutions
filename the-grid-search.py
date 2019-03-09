'''
for i in range(int(input())):
    rmain,cmain=map(int,input().split())
    mainmat=''
    for j in range(0,rmain):
        temp=list(map(str,input().split()))
        mainmat+=("".join(temp))
    print(mainmat)
    rpat,cpat=map(int,input().split())
    patmat=''
    for j in range(0,rpat):
        temp=list(map(str,input().split()))
        patmat+=("".join(temp))
    print(patmat)
    ctr=0
    pos=0
    cpat=[]
    for j in range(0,cpat):
        cpat.append(0)
    print(cpat)
    j=0
    while j<len(patmat):
        if (j+1)%rpat!=0:
            for k in range(pos,len(mainmat)):
                flag=0
                if patmat[j]==mainmat[k]:
                    pos=k+cpat
                    for l in range(k,k+cpat):
                        if patmat[k]!=mainmat[l]:
                            flag=1
                            break
                    if flag==0:
                        j+=cpat
                        
 '''
#include <iostream>

using namespace std;

int main() {
  int T, i;
  cin >> T;
  for (i = 1; i <= T; i++) {
    int R, C, r, c, flag = 0, final = 0;
    cin >> R >> C;
    char G[R][C];
    for (int j = 0; j < R; j++)
      for (int k = 0; k < C; k++)   
        cin >> G[j][k];
    cin >> r >> c;
    char P[r][c];
    for (int j = 0; j < r; j++)
      for (int k = 0; k < c; k++)
        cin >> P[j][k];

    for (int j = 0; j < R; j++)
      for (int k = 0; k < C; k++) {

        if (G[j][k] == P[0][0]) {
          int flag = 1;
          if (C - k >= c)
            for (int pr = 0; pr < r; pr++) {
              if (flag == 0)
                break;
              for (int pc = 0; pc < c; pc++) {

                if (G[j + pr][k + pc] == P[pr][pc]) {
                  if (pr == r - 1 && pc == c - 1)
                    final = 1;
                  flag = 1;
                } else {
                  flag = 0;
                  break;
                }
              }
            }
        }
      }
    if (final)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
}

                        
                    
            
    
