t=int(input())
for i in range(0,t):    
    over=[]
    x=input()
    n,p=x.split()
    n=int(n)
    p=int(p)
    yy=input()
    y=[]
    for j in range(0,len(yy)):
        y.append(yy[j])
    print(y)
    over=[]
    for k in range(0,n):
        over.append([])
        for l in range((k*6),(k*6)+6):
            if y[l]=='W':
                over[k].append(y[l])
            else:
                over[k].append(int(y[l]))
    print(over)
    pp=[]
    for m in range(0,p):
        pp.append(0)
    scheck=0
    for r in range(0,n):
        for p in range(0,6):
          
            if over[r][p]!='W':
                if over[r][p]==0:
                    pp[scheck]+=0
                elif over[r][p]==2 :
                    pp[scheck]+=2
                elif over[r][p]==4 :
                    pp[scheck]+=4
                elif over[r][p]==6 :
                    pp[scheck]+=6
                elif over[r][p]==1:
                    pp[scheck]+=1
                    if scheck%2==0:
                        scheck-=1
                        print("#1")
                    else:
                        scheck+=1
                        print("#2")
            elif over[r][p]=='W':
                 if scheck%2==0:
                     scheck-=2
                     print("#3")
                 else :
                     scheck+=1
                     print("#4")
        if r==n-1:
            if scheck%2==0:
                scheck-=1
            elif scheck%2!=0:
                scheck+=1
                
    print(scheck)            
    print(pp)
    cc=1
    print("Case",end=' ')
    print(cc,":")
    cc+=1
    player=1
    for u in range(0,len(pp)):
        if pp[u]==0:
            print("Player"," ",player,":","DNB")
            player+=1
        else:
            if player==scheck:  
                print("Player"," ",player,":",pp[u],"*")
                player+=1
                if scheck%2==0:
                    print("Player"," ",player,":",pp[u-1],"*")
                    player+=1
                else:
                    print("Player"," ",player,":",pp[u+1],"*")
                    player+=1
            else:
                print("Player"," ",player,":",pp[u],"*")
                player+=1
    
###### Pretty Simple Logic
#include <iostream>
#define OUT 1
#define NOTOUT 0
#define DNB (-1)
#using namespace std;

#int main()
#{
#int t,i; cin>>t; // for test case
#for(int r=1;r<=t;r++)
#{
#cout<<"Case "<<r<<":"<<endl; // display case number
#int n,p; cin>>n>>p; // n overs , p players
#int score[p+1],out[p+1]; // to implement 1 based indexing

#/*
#if out[i], =(-1) DNB : Batsman Did Not Batted
#= 0 NOTOUT : Batsman was onfield i.e., Not Out
#= 1 OUT : Batsman Out
#Note:Refer macros defined 
#*/

#for(i=0;i<=p;i++)
#{ score[i]=0; // score 0 for all players initially
#out[i]=DNB; // DNB as all Did Not Bat initially
#}
#char s[n*6+1]; cin>>s; // n*6 balls , 1 extra for '\0'
#int striker=1,nonstriker=2,ball=0; // start match
#out[striker]=out[nonstriker]=0; // out[i]=0 for onfield
#int overs=0,tocome=3,batsout=0; 
#// tocome for player no to bat next
#// batsout for no of batsmans out
#while(s[ball]!='\0') // if balls finished
#{
#if(s[ball]=='W') // if wicket goes
#{
##out[striker]=OUT; //striker batsman out
#striker=tocome++; //next man comes in
#batsout++;
#if((p-batsout)<=1) // if only 1 player is on field
#break; // game is over
#out[striker]=NOTOUT; // new player come as
#// onfield batsman
#}
#else
#{
#if(s[ball]%2==0) //if even runs,strike do not change
#{
#score[striker]+=int(s[ball]-48);
#// -48 to convert char to int
#// as int('0')=48
#}
#else // if odd runs
#{
#score[striker]+=int(s[ball]-48);
#swap(striker,nonstriker); //change strike
#}
#}
#if((ball+1)%6==0) // if (no of balls)%6=0,over changes
#{
#overs++; swap(striker,nonstriker); //strike changes
#}
#ball++; //next ball
#}

#// Print Scorecard
#for(int i=1;i<=p;i++)
#{
#if(out[i]==DNB) // Did Not Batted
#cout<<"Player "<<i<<": DNB"<<endl;
#else
#if(out[i]==NOTOUT) // Not Out print *
#cout<<"Player "<<i<<": "<<score[i]<<"*"<<endl;
#else // Played but got OUT
#cout<<"Player "<<i<<": "<<score[i]<<endl;

#}
#}

#return 0;
#}
        
        
        
