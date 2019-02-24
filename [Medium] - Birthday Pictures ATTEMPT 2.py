t=int(input())
for i in range(0,t):
    arr=list(map(int,input().split()))
    xxx=arr[0]
    del arr[0]
    arr.sort()
    #print(arr)
    ctr=0
    use=[]
    ptr=0
    final=[]
    while True:
        ctr+=arr[0]
        zzz=xxx-ctr
        if zzz%arr[1]==0:
            use.append([])
            use[ptr].append(ctr)
            use[ptr].append(zzz)
            use[ptr].append(arr[1])
            use[ptr].append(arr[0])
            ptr+=1
        if zzz%arr[2]==0:
            use.append([])
            use[ptr].append(ctr)
            use[ptr].append(zzz)
            use[ptr].append(arr[2])
            use[ptr].append(arr[0])
            ptr+=1
            
        if ctr==xxx:
            use.append([])
            use[ptr].append(ctr)
            use[ptr].append(zzz)
            use[ptr].append(arr[0])
            use[ptr].append(arr[0])
            ptr+=1
            break
        if ctr>xxx:
            break
    if not use:
        # NEXT LAYER
        ctr=0
        use=[]
        ptr=0
        final=[]
        while True:
            ctr+=arr[1]
            zzz=xxx-ctr
            if zzz%arr[0]==0:
                use.append([])
                use[ptr].append(ctr)
                use[ptr].append(zzz)
                use[ptr].append(arr[0])
                use[ptr].append(arr[1])
                ptr+=1
            if zzz%arr[2]==0:
                use.append([])
                use[ptr].append(ctr)
                use[ptr].append(zzz)
                use[ptr].append(arr[2])
                use[ptr].append(arr[1])
                ptr+=1
                
            if ctr==xxx:
                use.append([])
                use[ptr].append(ctr)
                use[ptr].append(zzz)
                use[ptr].append(arr[1])
                use[ptr].append(arr[1])
                ptr+=1
                break
            if ctr>xxx:
                break
        print(use)
        if not use:
            #NEXT LAYER
            ctr=0
            use=[]
            ptr=0
            final=[]
            while True:
                ctr+=arr[2]
                zzz=xxx-ctr
                if zzz%arr[0]==0:
                    use.append([])
                    use[ptr].append(ctr)
                    use[ptr].append(zzz)
                    use[ptr].append(arr[0])
                    use[ptr].append(arr[2])
                    ptr+=1
                if zzz%arr[1]==0:
                    use.append([])
                    use[ptr].append(ctr)
                    use[ptr].append(zzz)
                    use[ptr].append(arr[1])
                    use[ptr].append(arr[2])
                    ptr+=1
                    
                if ctr==xxx:
                    use.append([])
                    use[ptr].append(ctr)
                    use[ptr].append(zzz)
                    use[ptr].append(arr[2])
                    use[ptr].append(arr[2])
                    ptr+=1
                    break
                if ctr>xxx:
                    break
            #print(use)
            qqq=use.pop()
            #print(qqq)
            print((qqq[0]//qqq[3])+(qqq[1]//qqq[2]))
            
        else:
            #print(use)
            qqq=use.pop()
            #print(qqq)
            print((qqq[0]//qqq[3])+(qqq[1]//qqq[2]))
    else:
        #print(use)
        qqq=use.pop()
        #print(qqq)
        print((qqq[0]//qqq[3])+(qqq[1]//qqq[2]))
    

    
        
            
