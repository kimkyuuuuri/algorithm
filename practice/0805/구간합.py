n=5

array=[1,3,2,5,6]
sum_array=[0]
inter_sum=0

for i in array:
    inter_sum+=i
    sum_array.append(inter_sum)

print(sum_array)
print(sum_array[4]-sum_array[2])
