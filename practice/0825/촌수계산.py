n=int(input())
a,b = map(int, input().split())
m=int(input())
graph=[[] for i in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited=[-1] * (n+1)
visited[a]=0

def dfs(x):
    for i in graph[x]:
        if visited[i]==-1:
            visited[i]=visited[x]+1
            dfs(i)
dfs(a)
print(visited[b])
