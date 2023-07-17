def tron(n):
    j=[int(i) for i in str(n)]
    if j[0]==j[len(j)-1]:
        return 1
    else: return 0
x,y=list(map(int,input().split()))
t=0
for i in range(x,y+1):
    t+=tron(i)
print(t)

