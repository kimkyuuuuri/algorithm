n=int(input())
array=list(map(int,input().split()))
x=int(input())
array.sort()

count=0
left=0
right=n-1

while left!=right:   #좌측 포인트와 우측 포인트가 겹치게 되면 종료
    if array[left]+array[right]==x:
        count+=1
        left+=1
    elif array[left]+array[right]>x:
        right-=1
    else:
        left+=1

print(count)


