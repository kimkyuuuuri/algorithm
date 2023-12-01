# 배열의 길이, # 몇번 더하기 ? # 몇번 중복 가능?

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

# 가장 큰 수를 만든다.
array.sort(reverse=True)
first = array[0]
second = array[1]
result=0
flag=0

for i in range(m):
    if flag == k:
        result+=second
        flag=0
    else:
        result+=first
        flag+=1

        
    
print(result)
