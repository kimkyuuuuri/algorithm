n,k=map(int, input().split())

array=list(map(int, input().split()))
result=[True]*n
for i in range(k):
    a,b=map(int,input().split())
    a-=1
    b-=1
    if array[a]<array[b]:
        result[a]=False
    elif array[a]>array[b]:
        result[b]=False
    else:
        result[a]=False
        result[b]=False

print(result.count(True))
   
