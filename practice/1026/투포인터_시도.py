n=int(input())
array=list(map(int,input().split()))
k=int(input())

# end를 하나씩 늘려가고
# first를 하나씩 뺸다
end=0
now_sum=0
count=0

for i in range(n):
    while now_sum < k and  end<n:
        now_sum+=array[end]
        end+=1
  
    if now_sum == k:
        count+=1
    now_sum-=array[i]

        
print(count)
