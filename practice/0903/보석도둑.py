import sys
import heapq
input=sys.stdin.readline
n,k = map(int, input().split())
array=[]
bag=[]
index=0
answer=0
for i in range(n):
    m,v = map(int, input().split())
    array.append([m,v])

array.sort(key=lambda x:x[1], reverse=True)
array.sort(key=lambda x:x[0])

for j in range(k):
    bag.append(int(input()))
bag.sort()
temp=[]

# temp가 비어있으면? 해결
# 시간 초과  o(n^2)이됨. 
for i in bag:
    while index< len(array) and array[index][0]<=i:
        heapq.heappush(temp, -array[index][1])
        index+=1
    if temp:
        answer-=heapq.heappop(temp)
    
print(answer)
 
