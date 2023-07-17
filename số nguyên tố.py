n=4
def sont(n):
    a=[True]*(n+1)
    for i in range(2,len(a)):
        if a[i]==True:
            for k in range(i*2,len(a),i):
                a[k]=False
    
    return a[n]
print(sont(n))
#for i in range(2,len(a)):
 #   if  a[i]== True:
  #      print(i,end=" ")
