import heapq
n=int(input())
q=[]

for i in range(n):
    heapq.heappush(q,int(input()))

result=0


while len(q)!=1:
    first=heapq.heappop(q)
    second=heapq.heappop(q)
    first_sum=first+second
    result+=first_sum
    heapq.heappush(q,first_sum)
    


print(result)
#print(q[0])
    
      
