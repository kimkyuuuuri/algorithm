import heapq
import sys
input = sys.stdin.readline

INF=int(1e9)
n,m=map(int,input().split())
##
start=int(input())
##
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            #그래프에 저장된 것 + 큐에 저장된 최단 거리 
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)

for i in range(1,n+1):
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])
            
        
        
    

