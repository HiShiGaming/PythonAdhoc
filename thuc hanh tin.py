import math
def san(n):
    b=[True]*(n+1)
    b[0]=False
    b[1]=True
    c=[]
    for i in range(2,n):
        if b[i]== True:
            for z in range(i*2,n+1,i):
                b[z]=False
    for i in range(1,n+1):
        if b[i]==True:
            c.append(i)
    return c

print(math.gcd(6,3))
