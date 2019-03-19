t=int(input())
def p(t):
    n=0
    while t!=0:
                x=[0,0,0]
                z=2**int(n/26)
                y=n%26
                if  y>=11:
                        x[2]=z
                elif y==0:
                        x[2]=2**int((n-1)/26)
                elif y<=2:
                        x[0]=z
                else:
                        x[1]=z
                for i in x:
                        print(i,end=" ")
                print()
                t=t-1
                n+=1

p(t)
