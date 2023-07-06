import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        #거리랑 현재 노드
        dist,now = heapq.heappop(q)
        #짧은 순으로 나오기때문에 거리가 작으면 이미 처리한 노드라고 볼 수 있다. 
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(1)
for i in range(1,n+1):
    if distance[i] == INF:
        print("무한대")
    else:
        print(distance[i])
            
    
