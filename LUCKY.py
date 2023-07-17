n,k=map(int,input().split())
if n!=0:
    test=list(map(int,input().split()))
    rutgon=list(set(test))
    cout=[]
    ans=0
    for i in range(len(test)):
        for j in range(i+1,len(test)):
            if abs(test[i]+test[j])==k:
                ans+=1#test.count(rutgon[j])            
    print(ans)
else:
    print(0)
