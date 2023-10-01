import heapq
n=int(input())
array=[]
q=[]

for i in range(n):
    n=int(input())
    array.append(n)
    if i!=0:
        heapq.heappush(q,[-n,i])
        
answer=0

while q:
    now=heapq.heappop(q)
    if array[0]<=-now[0]:
        array[0]+=1
        now[0]+=1
        heapq.heappush(q,[now[0],now[1]])
        answer+=1
    else:
        break

print(answer)



    
