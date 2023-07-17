def imherenow111(n):
    trung = [True] * (n + 1)
trung[0] = False
trung[1] = False
for i in range(2, int(n ** 0.5) ):
if trung[i]:
for t in range(i * i, n + 1, i):
trung[t] = False
nottrung = []
for i in range(2,n + 1):
if trung[i]:
nottrung.append(i)
return nottrung
