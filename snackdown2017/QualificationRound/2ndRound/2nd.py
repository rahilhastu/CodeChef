for _ in range(int(raw_input())):
    n = int(raw_input())
    ro1 = raw_input()
    ro2 = raw_input()
    o=[]
    index = True
    no = False
    cou=0
    r1=[]
    r2=[]
    for i in xrange(n):
        r1.append(ro1[i])
        r2.append(ro2[i])

    for i in range(n):

        if (index and r1[i]=='#' and r2[i]=='#'):
            index = False
            no = True
            cou+1

        elif (index and r1[i]=='#' and r2[i]!='#'):
            index = True
            no = True
            cou+=1

        elif (not index and r2[i]=='#' and r1[i]=='#'):
            index=True
            no = True
            cou+=1

        elif (not index and r2[i]=='#' and r1[i]!='#'):
            index = False
            no = True   
            cou+=1

        elif (r1[i]!='#' and r2[i]!='#'):
            no = True
            index = True
            #print r1.index("#",i-1)
            try:
                if (cou >0 and (r1.index("#",i)>-1 or r2.index("#",i)>-1)):
                    no = False
                    break
            except ValueError as e:
                no = True
                break
        

        elif (cou ==0 and r2[j]=='#'):
            no = True
            index = False
        else:
            no = False
            break

    if (not no ):
        print 'no'
    else:
        print 'yes'