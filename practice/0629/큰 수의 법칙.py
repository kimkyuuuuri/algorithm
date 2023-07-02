n,m,k = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

count=k
flag=0
result=0

for i in range(m):
    if count!=0:
        result += arr[-1]
        count-=1
    else:
        result += arr[-2]
        count=k
         
    
print(result)
