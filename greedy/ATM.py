n=int(input())
array=list(map(int,input().split()))
array.sort()
result=0
count=n

for i in range(n):
    result+=array[i]*count
    count-=1
    
print(result)
