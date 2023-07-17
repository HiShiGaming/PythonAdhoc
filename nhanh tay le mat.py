
def nhanhtaylemat(A):
    s=0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]==A[j]:
                s+=1
    return print(s)
n=int(input())
a=input()
Z=a.split(" ")
Z.pop()
Z=list(map(int,Z))
nhanhtaylemat(Z)
