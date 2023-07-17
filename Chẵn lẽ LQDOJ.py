n=int(input())
a=[int(input()) for i in range(n)]
def sl(n):
    b=[False]*len(str(n))
    a=[int(i) for i in str(n)]
    if len(str(n))==1:
        if n%2 !=0:
            return print("YES")
        else: return("NO")
    for i in range((len(str(n))+1),2):
        b[i]=True
    for i in range(len(a)+1):
        if (a[i]%2 !=0 and b[i]==True) or (a[i]%2 ==0 and b[i]==False):
            return print("NO")
    return print("YES")
def gay(n):
    b=[True]*len(str(n))
    a=[int(i) for i in str(n)]
    for i in range(len(str(n)),2):
        b[i]=True
    for i in range(1,len(str(n))):
        if a[i] %2 ==0 and b[i]==False:
            
                return print("NO")
        if a[i] % 2 !=0 and b[i]==True:
                return print("NO")
    return print("YES")
def bruh(n):
    a=[int(i) for i in str(n)]
    for i in range(1,len(str(n))+1):
        if i % 2 != 0 and a[i-1]%2 ==0:
            return print("NO",)
        if i%2 == 0 and a[i-1] % 2 !=0:
            return print("NO",)
    return print("YES")
for i in a:
    bruh(i)

        
    
