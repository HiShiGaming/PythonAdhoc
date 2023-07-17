a=input()
o=a.split('+')
z=[int(i) for i in o]
n=list(sorted(z))
x="+".join(str(n))
print(x)

