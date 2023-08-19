import sys
import heapq
input=sys.stdin.readline

n=int(input())
first=int(input())
array=[]
for i in range(n-1):
    heapq.heappush(array, -int(input()))


count=0
while array and -array[0]>=first:
    num= -heapq.heappop(array)
    num-=1
    heapq.heappush(array, -num)
    count+=1
    first+=1
  
print(count)
    

