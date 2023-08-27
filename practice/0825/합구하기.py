import sys
input = sys.stdin.readline
n=int(input())
array = list(map(int, input().split()))

#prefix 구하기
temp = [0]
temp_sum=0

for i in  array:
    temp_sum+=i
    temp.append(temp_sum)

m=int(input())
for i in range(m):
    a,b = map(int, input().split())
    print(temp[b]-temp[a-1])
