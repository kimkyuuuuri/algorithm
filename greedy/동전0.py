n,k=map(int,input().split())
array=[]
result=0
for i in range(n):
    array.append(int(input()))

for j in range(n-1,-1,-1):
   
    result+=k//array[j]
    k=k%array[j]

print(result)
    
    
