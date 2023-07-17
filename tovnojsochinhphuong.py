def day(l,r):
    c=[]
    if l==r:
        if (l**0.5).is_integer():
            return c.append(l)
        else: return " " 
    for i in range(int(l**0.5),int(r**0.5)+1) :
        c.append(i**2)
    if c[0]<l:
        c.remove(c[0])
    if c==[]:
         return " "
    if c[len(c)-1] > r:
        c.remove(c[len(c)-1])
    return(c)
n=int(input())
c=[[]]*n
for i in range(n):
    l,r=list(map(int,input().split()))
    c[i]=day(l,r)
for y in range(n):
        print (" ".join([str(i) for i in c[y]]))