n=int(input())
array=list(map(int, input().split()))
array.sort()
result=0
for i in range(n):
    for j in range(i+1):
        result+=array[j]
    
print(result)
