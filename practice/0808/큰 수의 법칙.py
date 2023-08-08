n, m, k = map(int, input().split())
array=[]
result=0
count=0

array = list(map(int, input().split()))
array.sort(reverse=True)

for i in range(m):
    if count == k-1:
        count=0
        result+=array[1]
        continue
    
    count+=1
    result+=array[0]
    
print(result)
