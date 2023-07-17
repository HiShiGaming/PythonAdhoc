a=[-4,2,3,5,-5,6,8,9,7,-3,8,255,2,62,25,25,2,5,2,]
def timsoduonglientiep(a):
    l,r,i,cucdai,day=0,0,0,0,0
    for i in range(i,len(a)):
        if a[i] >0:
            l=i
            r=i      
            for f in range(l,len(a)):
                if a[f]>=0:
                    r+=1
                else:
                    i=r
                    break                           
            if cucdai< len(a[l:r]):
                cucdai = len(a[l:r])
                day=a[l:r]
    return(print(day))
timsoduonglientiep(a)

