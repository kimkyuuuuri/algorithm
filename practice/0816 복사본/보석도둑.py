import heapq
n,k = map(int, input().split())
heap=[]
bag=[]
for i in range(n):
    a,b=map(int, input().split())
    heapq.heappush(heap, (-b,a))

for i in range(k):
    bag.append(int(input()))
bag.sort()
    

result=0
index=0


while len(heap)>0 and index<k:
    now = heapq.heappop(heap)

    #반복문 두개를 사용할 수 없음. 
 
    for i in range(len(bag)):
        if now[1]<=bag[i]:
            bag.pop(i)
            result+=now[0]*-1
            index+=1
            break
   
print(result)
