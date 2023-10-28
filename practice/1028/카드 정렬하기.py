n=int(input())
array=[]
result=0

for i in range(n):
    array.append(int(input()))

array.sort()
interval_sum=array[0]

for i in range(1,n):
    temp=interval_sum+array[i]
    result+=temp
    interval_sum=temp
   

print(result)
    
