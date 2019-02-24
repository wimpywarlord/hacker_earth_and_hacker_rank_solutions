r,c,n=map(int,input().split())
ini=[]
for i in range(0,r):
    s=input()
    ini.append([])
    for j in range(0,len(s)):
        ini[i].append(s[j])
copy=[]
for i in range(0,r):
    copy.append([])
    for j in range(0,c):
        copy[i].append('0')
#print(copy)
for i in range(0,r):
    for j in range(0,c):
        #print(ini[i][j])
        if ini[i][j]=='.':
            pass
        elif i==0 and j!=0 and j!=c-1:
            #if ini[i][j]=='0' :
                copy[i][j]='.'
                copy[i+1][j]='.'
                copy[i][j+1]='.'
                copy[i][j-1]='.'
                #print(1)
        elif i==r-1 and j!=0 and j!=c-1:
            #if ini[i][j]=='0':
                copy[i][j]='.'
                copy[i-1][j]='.'
                copy[i][j+1]='.'
                copy[i][j-1]='.'
                #print(2)
        elif i==0 and j==0:
            #if ini[i][j]=='0':
                copy[i][j]='.'
                copy[i+1][j]='.'
                copy[i][j+1]='.'
                #print(3)
        elif i==0 and j==c-1:
            #if ini[i][j]=='0':
                copy[i][j]='.'
                copy[i+1][j]='.'
                copy[i][j-1]='.'
                #print(4)
        elif j==0 and i==r-1:
            #if ini[i][j]=='0':
                copy[i][j]='.'
                copy[i-1][j]='.'
                copy[i][j+1]='.'
                #print(5)
        elif j==c-1 and i==r-1:
            #if ini[i][j]=='0':
                copy[i][j]='.'
                copy[i-1][j]='.'
                copy[i][j-1]='.'
                #print(6)
        elif j==0 and i!=0 and i!=r-1:
            #if ini[i][j]=='0':
                copy[i][j]='.'
                copy[i+1][j]='.'
                copy[i-1][j]='.'
                copy[i][j+1]='.'
                #print(7)
        elif j==c-1 and i!=0 and i!=r-1:
            #if ini[i][j]=='0':
                copy[i][j]='.'
                copy[i][j-1]='.'
                copy[i+1][j]='.'
                copy[i-1][j]='.'
                #print(8)
        elif j!=0 and j!=c-1 and i!=0 and i!=r-1:
            copy[i][j]='.'
            copy[i][j+1]='.'
            copy[i][j-1]='.'
            copy[i+1][j]='.'
            copy[i-1][j]='.'
            #print(9)
if n%2!=0:
    for i in range(0,len(copy)):
        for j in range(0,len(copy[i])):
            if j==len(copy[i])-1:
                print(copy[i][j],end=' ')
            else:
                print(copy[i][j],end='')
        print()
else:
    for i in range(0,len(ini)):
        for j in range(0,len(ini[i])):
            if j==len(ini[i])-1:
                print(ini[i][j],end=' ')
            else:
                print(ini[i][j],end='')
        print()
#ITS ALL CAPITAL O
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
'''
void print_board(char *bombs, int len, int C) {
    for(int i = 0; i < len; i++) {
        if(i && !(i%C))
            printf("\n");
        if(bombs != NULL) {
            if(bombs[i] == 0)
                printf(".");
            else
                printf("O");
        }
        else
            printf("O");
    }
}

void detonate(char *bombs1, char *bombs2, int len, int C) {
    for(int i = 0; i < len; i++) {        
        if(bombs1[i] == 1) {
            bombs2[i] = 0;
            if((i+1) % C) 
                bombs2[i+1] = 0;
            if(i%C)
                bombs2[i-1] = 0;
            if(i-C >= 0) 
                bombs2[i-C] = 0;
            if(i+C < len) 
                bombs2[i+C] = 0;
        }
    }
}

int main() {
    int R, C, N;
    scanf("%d %d %d", &R, &C, &N);
    int len = R*C;
    char *bombs1 = (char*)calloc(len, sizeof(char));
    char *bombs2 = (char*)calloc(len, sizeof(char));
    char c;
    
    if(!(N % 2)) {
        print_board(NULL, len, C);
        return 0;
    }
    
    for(int i = 0; i < len; i++) {
        scanf(" %c", &c);
        if(c == 'O')
            bombs1[i] = 1;
        else if(c == '.')
            bombs2[i] = 1;    
    }
    
    if(N == 1) {
        print_board(bombs1, len, C);
        return 0;
    }
    
    detonate(bombs1, bombs2, len, C);
    memset(bombs1, 1, len);
    detonate(bombs2, bombs1, len, C);
    
    if (N%4 == 3)
        print_board(bombs2, len, C);
    else
        print_board(bombs1, len, C);
    return 0;
}'''
