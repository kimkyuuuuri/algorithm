import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(3)]
distance = [INF]*(n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start]=0
    # heap에서 꺼내기 시작한다.
    while q:
        dist, now = heapq.heqppop(q)
        if distance[now] < dist:
            continue

        # 거리가 첫번쨰에 저장되어 있음.
        for i in graph[now]:
            cost = dist + i[1]

        # 거리가 현재 저장된 거리보다 작다면, 갱신
        # 큐도 갱신 
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

        
        

print(graph)

