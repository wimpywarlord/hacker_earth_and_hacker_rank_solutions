order_number=[]
score=[]
import copy
for i in range(int(input())):
    order_number.append([])
    a,b=map(int,input().split())
    order_number[i].append(a)
    order_number[i].append(b)
    score.append(a+b)
copy=copy.deepcopy(order_number)
#print(copy)
order_number.sort(key=lambda x:x[0])
score.sort()
#print(score)
print(order_number)
final=[]
for i in range(0,len(score)):
    for j in range(0,len(order_number)):
        if order_number[j][0]+order_number[j][1]==score[i]:
            final.append([order_number[j][0],order_number[j][1]])
            order_number[j][0]=-100
            order_number[j][1]=-100
            break
print(final)
print(copy)
for i in range(0,len(final)):
    for j in range(0,len(copy)):
        #print(final[i][0],final[i][1])
        #print(copy[j][0],copy[j][1])
        if final[i][0]==copy[j][0] and final[i][1]==copy[j][1]:
            copy[j][0]=-100
            copy[j][1]=-100
            print(j+1,end=' ')
            break
    #print()
    #print(copy)
    #print(final)
