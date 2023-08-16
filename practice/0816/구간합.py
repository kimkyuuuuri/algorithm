n=5
data = [10,20,30,40,50]

#prefix sum 구하기
prefix_sum=0
array=[0]
for i in data:
    prefix_sum+=i
    array.append(prefix_sum)

print(array)
print(array[3]-array[0])
 
