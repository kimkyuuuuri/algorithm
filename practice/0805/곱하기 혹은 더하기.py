n=input()
result=int(n[0])

for i in range(1,len(n)):
    if n[i] ==0 or n[i]==1 or result==0:
        result+=int(n[i])
    else:
        result*=int(n[i])
        
print(result)
