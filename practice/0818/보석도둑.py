import sys
import heapq
n,k=map(int, input().split())
input=sys.stdin.readline
bosuk=[]
bag=[]
temp=[]
result=0
for i in range(n):
    a,b = map(int, input().split())
    bosuk.append((a,b))

for i in range(k):
    bag.append(int(input()))

bosuk.sort()
bag.sort()

for i in bag:
    index=0
    while bosuk and bosuk[0][0]<= i :
        heapq.heappush(temp,-bosuk[0][1])
        heapq.heappop(bosuk)
    if temp:
        result+=(-1)*heapq.heappop(temp)
        
    
print(result)


