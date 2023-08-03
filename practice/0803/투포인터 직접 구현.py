n=5
m=5

# array 길이 5
# 구해야하는 합은 5

data = [1,2,3,2,5]
len_sum=0
end=0
count=0

for start in range(len(data)):
    while len_sum <n and end<n:
        len_sum+=data[end]
        end+=1
        
    if len_sum==n:
            count+=1
            
    len_sum-=data[start]


print(count)

    
        
