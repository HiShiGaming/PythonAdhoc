a=[]
n=int(input('n='))
b=[0]*50
print(b)
for i in range (n):
    a.append(int(input()))
print("day vua nhap la:",a)
for i in range(len(a)):
    b[a[i]]+=1
c=max(b)
for i in a:
    if b[i] == c:
        print("so xuat nhien nhieu nhat là số:", i,",",c,"lan")
        break
    
