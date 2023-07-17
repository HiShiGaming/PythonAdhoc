#l,r= list(map(int,input().split()))
n=int(input())
soDaoNguoc= 0
while n > 0:
        chuSoCuoi = n % 10
        soDaoNguoc = soDaoNguoc * 10 + chuSoCuoi
        n = n // 10
        print(soDaoNguoc)
