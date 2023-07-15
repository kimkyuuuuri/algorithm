n,m = map(int, input().split())
array = list(map(int, input().split()))
count_array=[0]*(m+1)
result=[0]*(m+1)
count=0
for i in array:
    count_array[i]+=1

for i in count_array:
    n-=count_array[i]
    count+=count_array[i]*n


print(count)


