a=[]
n=int(input())
for i in range(n):
    a.append(int(input()))


def th1(a):
    for n in range(1,len(a)):
        if a[n-1]>a[n]:
           return print("NO")
    return print("YES")

th1(a)