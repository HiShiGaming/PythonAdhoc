a=[]
c=0
n=int(input("Nhap so luong phan tu:"))
def tonguocso(z):
    f=[]
    m=0
    for i in range(1,z):
        f.append(i)
    for k in f:
        if z % k ==0:
            m+=k
    if m == z:
        return 1
    else:
        return 0       
for i in range(n):
    a.append(int(input()))
for k in a:    
    c+=tonguocso(k)
print("cac so hoan hao trong day la:",c)
    
    
