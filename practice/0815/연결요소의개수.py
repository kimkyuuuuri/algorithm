import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())

graph=[[] for i in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,x,visited):
    visited[x]=True
    for now in graph[x]:
        if not visited[now]:
            dfs(graph, now, visited)

answer=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        answer+=1
    

print(answer)
    

