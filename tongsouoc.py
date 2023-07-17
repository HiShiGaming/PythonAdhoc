n=int(input())
a=[]
for i in range(1,round(n**0.5)+1):
    if n % i==0:
        a.append(i),a.append(int(n/i))
print(sum(list(set(a))))