n,m = map(int, input().split())
array = list(map(int, input().split()))

result=0
end=0
interval_sum=0

for start in range(n):
    while end <n and interval_sum<m:
        interval_sum+=array[end]
        end+=1
        
    if interval_sum==m:
        result+=1
        
    interval_sum-=array[start]

print(result)
        
