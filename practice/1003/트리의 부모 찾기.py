import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n=int(input())
graph=[[] for i in range(n+1)]
global visited;
visited= [False]*(n+1)

for i in range(n-1):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(now):
    
    for i in graph[now]:
        if not visited[i]:
            visited[i]=now
            dfs(i)


dfs(1)
for i in range(2, n+1):
    print(visited[i])
