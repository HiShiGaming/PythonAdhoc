def logic(n):
    c=n
    #if len(str(sum(map(int,str(c).split()))))==2:
        #return sum(map(int,str(c).split()))
    while len(str(c))!=1:
        c=sum(map(int,str(c).split()))
        return c
def logic1(n):
    if len(str(sum(a)))==1:
        return sum(a)
    cnt = sum(a)
    while len(str(cnt))!=1:
        cnt=sum(int (i) for i in str(cnt))
    return cnt
c=map(str,input().split())
a=(int(i) for i in c)
print(logic1(a))
        
        
