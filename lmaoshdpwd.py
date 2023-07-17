import math
def pro(n):
	b=[]
	a=math.sqrt(n)
	for i in range(1,int(a)+1):
		if n%i==0:
			b.append(i)
			if n//i!=i:
				b.append(n//i)				
	return b

def nhanhtaylemat(A):
    s=0
	for i in range(len(A)+1):
        for j in range(i,len(A)+1):
            if A[i]==A[j]:
                s+=1
    return print(s)                                          
def ktcp(n):
    for i in range(n+1):
        if i**2 == n:
            return print("YES")
    return print("NO")
def gay(n):
	import math
	if  math.sqrt(n) == int :
		return print("YES")
	else:
		return print("NO")

Z=[1,1,5,3,5,1,3]
nhanhtaylemat(Z)
