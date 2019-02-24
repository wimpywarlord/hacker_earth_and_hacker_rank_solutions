"""n=int(input())
namelist=[]
d=dict()
for i in range(0,n):
    x=input()
    name,time=x.split()
    time=int(time)
    namelist.append([])
    namelist[i].append(name)
    namelist[i].append(time)
    d[name]=[0,0]
final=[]
for i in range(0,n):
    d[namelist[i][0]][0]+=namelist[i][1]
    d[namelist[i][0]][1]+=1
b=d.keys()
g=[]
for i in b:
    g.append(i)
print(g)
for i in range(0,len(d)):
    final.append([])
    final[i].append(g[i])
    final[i].append(d[g[i]][0])
    final[i].append(d[g[i]][1])

print(final)

# Python code to sort the tuples using second element  
# of sublist Function to sort using sorted() 
def Sortfre(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    return(sorted(sub_li, key = lambda x: x[1],reverse=True))    
# Driver Code
def check(q):
    global final
    flag=0
    for i in range(0,len(final)):
        if final[i][2]==q:
            flag=1
    if flag==0:
        return False
    else:
        return True
    
print(Sortfre(final))
ctr=1
for i in range(0,len(final)):
    xx=len(final)
    for j in range(0,xx):
        if check(final[j][2])==False:
            print(ctr,final[j][0])
            del final[j]
            ctr+=1
        else:
            pass"""
# Leaderboard Standings
 
N = int(input())
contestants = {}
for _ in range(N):
    name, time = input().split()
    time = int(time)
    if name in contestants:
        contestants[name]["points"] += 100
        contestants[name]["time"] += time
    else:
        contestants[name] = {"points": 100, "time": time}
print(contestants)
leaderboard = []
for name in contestants:
    leaderboard.append([name, contestants[name]["points"], contestants[name]["time"]])
leaderboard.sort(key=lambda x: (-x[1], x[2], x[0]))
 
place = 0
for name, points, time in leaderboard:
    place += 1
    print(place, name)
 




            
    
    
    
    
