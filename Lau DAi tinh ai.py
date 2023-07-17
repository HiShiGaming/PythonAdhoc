n= int(input())
b=[[]]*n
for i in range(n):
    a=list(map(int,input().split()))
    c=[]
    for z in range(len(a)):
        if a[0]== 0 and a[1]==0 and a[2]==0:
            c=[1,1,1]
            break
        if a[z] < max(a):
            c.append(max(a)-a[z]+1)
        else:
            c.append(max(a)-a[z])
    b[i]=c
for o in range(n):
    print(" ".join(list(map(str,b[o]))))

             
