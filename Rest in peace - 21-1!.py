for i in range(int(input())):
    n=input()
    if int(n)%21==0:
        print("The streak is broken!")
    else:
        if n.count("21")>0 :
             print("The streak is broken!")
        else:
            print("The streak lives still in our heart!")
            
