def timgacholaptontg(n,k):    
    m=0
    c=0
    for i in range(1,k,2):
        m+=1
    while m > n:
        m-=1
        c+=4
    chicken=(k-c)//2
    dog=c//4
    if chicken+dog == n and chicken*dog > 0:  
        return(print(chicken,dog))
    else:
        return print(-1)
def timgacho2(n,k):
    changa=n*2
    chancho=k-changa
    cho= chancho//2
    ga=n-cho
    if ga <0 or cho <0:
        return print(-1)
    else:
        return print(ga,cho)
n=int(input())
k=int(input())
timgacho2(n,k)
    
    
