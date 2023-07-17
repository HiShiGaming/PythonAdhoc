def gg(n):
    import math
    for i in range(2,n):
        if n % i**2==0:
            return print(i, n//i**2)
n=int(input())
a=[int(input()) for i in range(n)]
for h in a:
    gg(h)
