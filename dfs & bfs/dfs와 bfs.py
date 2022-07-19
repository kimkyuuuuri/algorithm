#dfs 코드
from collections import deque
n,e,s=map(int,input().split())
visited=[False]*e
graph=[]
for i in range(e):
    graph.append(list(map(int, input().split())))


def dfs(graph,v,visited):
    visited[v]=True
    print(v,end='')
    for i in graph[v]:
        if not visited[i] :
            dfs(graph,i,visited)

dfs(graph,1,visited)

visited2=[False]*e

def bfs(graph,start,visited2):
    queue=deque([start])
    visited2[start]=True
    while queue:
        v=queue.popleft()
        print(v,end='')
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i]=True

bfs(graph,1,visited2)
