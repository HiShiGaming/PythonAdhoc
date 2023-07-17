n=int(input())
a=[]
c=[]
def ch(a):
    if a == a[::-1]:
        return "Yes"
    else: return "No"
for t in range(n):
    z=input()
    a=[int(i) for i in z]
    c.append(ch(a))
for m in c:
    print(m)



        
