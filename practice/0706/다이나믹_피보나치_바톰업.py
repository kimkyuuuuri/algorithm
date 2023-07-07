d=[0]*1001
d[1]=1
d[2]=1

def fibo(x):
    
    for i in range(2,x):
        d[i+1]=d[i]+d[i-1]
        
    return d[x]


print(fibo(7))
