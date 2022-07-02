n=int(input())
#배열 입력받기 (파이썬은 크기를 지정하지 않아도 됨.)
data=list(map(int,input().split()))
data.sort()

result=0
count=0

for i in data:
    count+=1
    if count>=i:
        result+=1
        count=0

print(result)
