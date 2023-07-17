n= int(input())
a=[]
def nt(n):
    b=[True]*n
    b[0]=False
    b[1]= False
    for i in range(2,len(b)):
        if b[i] != False:
            b[i]=i
            for z in range(i*2,len(b),i):
                b[z] =False
            
    return b
d=list(dict.fromkeys(nt(1000)))
for i in range(n):
   a.append(int(input()))
for h in a:
    print(d[h])


