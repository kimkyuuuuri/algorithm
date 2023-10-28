n=int(input())

result=0
flag=0

while n>=0:
    if n%5==0:
        result+=int(n//5)
        flag=1
        break
        
   
    n-=3
    result+=1

if n!=0 and flag==0:
    print(-1)
else:
    print(result)
    
    
