n=int(input())
array=list(map(int, input().split()))
array.sort()
result=0
for i in range(n):
    print(i)
    print("이건 i")
    for j in range(i+1):
        print(j)
       
        result+=array[j]
    
print(result)
