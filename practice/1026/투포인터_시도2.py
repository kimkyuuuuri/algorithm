n=int(input())
array=list(map(int,input().split()))
k=int(input())

# end를 하나씩 늘려가고
# first를 하나씩 뺸다

# 이거는 연속 ! 
count=0
interval_sum=0
end=0

for start in range(n):
    while interval_sum<k and end<n:
        interval_sum+=array[end]
        end+=1
    if interval_sum ==k:
        count+=1
    interval_sum -= array[start]
print(count)
