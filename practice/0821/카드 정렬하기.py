import heapq
n=int(input())
array=[]
answer=0
for i in range(n):
    heapq.heappush(array,int(input()))

while len(array)>=2:
    now=heapq.heappop(array) + heapq.heappop(array)
    heapq.heappush(array,now)
    answer+=now
    
print(answer)
