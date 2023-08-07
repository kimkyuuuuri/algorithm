from collections import deque
import sys
n, m, k, x = map(int, input().split())
graph=[[] for _ in range(n+1)]
visited=[-1]*(n+1)
visited[x]=0

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def bfs(graph, start, visited):
    que=deque([])
    que.append(start)
    while que:
        v=que.popleft()
        for i in graph[v]:
            if  visited[i]==-1:
                visited[i]=visited[v]+1
                que.append(i)
                

bfs(graph,x,visited)
flag=0

for i in range(1,n+1):
    if visited[i]==k:
        flag=1
        print(i)
        
if flag==0:
    print(-1)
    
