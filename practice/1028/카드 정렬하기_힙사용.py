import sys
input=sys.stdin.readline
n=int(input())
array=[]

import heapq
for i in range(n):
    heapq.heappush(array,int(input()))
 
result=0

while len(array)>=2:
    first=heapq.heappop(array)
    second=heapq.heappop(array)
    temp=first+second
    result+=temp
    heapq.heappush(array,temp)

print(result)
    
