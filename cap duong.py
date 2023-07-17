def da(a):
    b=[]
    c=[]
    z=0
    for i in a:
        if i > 0 :
            b.append(i)
        else:
            c.append(i)
    for m in range(len(b)):
        for j in range(m+1,len(b)):
            z+=1
    for p in range(len(c)):
        for u in range(p+1,len(c)):
            z+=1
    return z
def capduong(a):
    b= [True]*len(a)
    for i in a:
        if  i< 0:
            b[i]== False
    

