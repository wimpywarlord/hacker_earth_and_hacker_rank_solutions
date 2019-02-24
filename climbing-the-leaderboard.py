'''n=int(input())
score=list(map(int,input().split()))
#print(score)
n2=int(input())
alice=list(map(int,input().split()))
rank=[]
ctr=1
for i in range(0,len(score)):
    if i!=len(score)-1:
        if score[i]>score[i+1]:
            rank.append(ctr)
            ctr+=1
        else:
            rank.append(ctr)
    else:
        rank.append(ctr)
#print(rank)
alice.sort(reverse=True)
#print(alice)
ans=[]
pos=0
for i in range(0,len(alice)):
    if alice[i]>=max(score):
        ans.append(1)
        #print(1)
    elif alice[i]<min(score):
        ans.append(rank[len(rank)-1]+1)
        #print(rank[len(rank)-1]+1)
    elif alice[i]==min(score):
        ans.append(rank[len(rank)-1])
        #print(rank[len(rank)-1])
    else:
        for j in range(pos,len(score)):
            if alice[i]==score[j]:
                ans.append(rank[j])
                #print(rank[j])
                pos=j
                break
            
            elif score[j]>alice[i]>score[j+1]:
                ans.append(rank[j]+1)
                #print(rank[j]+1)
                pos=j
                break
ans2=list(reversed(ans))
for i in range(0,len(ans2)):
    print(ans2[i])
        '''

        
    
    #!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input().strip())
    scores = sorted(list(set(list(map(int, input().strip().split(' '))))), reverse=True)
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    scores.append(0)
    l = len(scores)
    # Write Your Code Here
    for a in alice:
        while (l > 0) and (a >= scores[l-1]):
            l -= 1
        print(l+1)
