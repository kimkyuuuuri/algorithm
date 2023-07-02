n=1260
coin = [500,100,50,10]
result=0
print(result)
for i in range(4):
    result+=n//coin[i]
    n=n%coin[i]

  
print(result)
    
