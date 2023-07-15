n,m = map(int, input().split())
array = list(map(int, input().split()))
count_array=[0]*(m+1)
result=[0]*(m+1)
count=0
for i in array:
    count_array[i]+=1

for i in range(1,len(count_array)):
    another_count=0
    for j in range(i+1,len(count_array)):
        
        another_count+=count_array[j]
  
    count+= count_array[i]*another_count


print(count)


