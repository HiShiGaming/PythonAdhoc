n=int(input('N='))
a=[]
def day(n,a,x):
    m=0
    for i in range(len(a)):
        if a[i]==x:
            m+=1
    for i in range(len(a)):
        if i == len(a)-1:
            break
        if a[i]>a[i+1]:
            return print(m,"Không")            
    return print(m,"Có")
for i in range(n):
    a.append(int(input('A=')))
x=int(input('X='))

day(n,a,x)



        
        
        
        
        
        


