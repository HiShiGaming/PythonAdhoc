n=int(input())
m=list(map(int,input().split()))
l=list(reversed(sorted(m)))
t=0
print(l)
for i in range(len(l)):
    t=l[i]+l[i+1]+l[i+2]
    if 