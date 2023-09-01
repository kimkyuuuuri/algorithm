import sys
import heapq
input= sys.stdin.readline
n=int(input())
array=[]
answer=1
for i in range(n):
    a,b=map(int, input().split())
    array.append((a,b))

array.sort()
que=[]
#heapq.heappush(que,array[0][0])

# 원소가 하나씩 들어올 때마다 
for i in range(n):
    while que and que[0]<=array[i][0]:
        heapq.heappop(que)
    heapq.heappush(que,array[i][1])
    answer=max(answer,len(que))

print(answer)
    


    
    
    
        
    
