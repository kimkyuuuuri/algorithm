from collections import  deque
import sys
input=sys.stdin.readline
n, m, k, x = map(int, input().split())
visited=[-1]* (n+1)
graph=[[] for i in range(n+1)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

# 최단거리니까 bfs
que=deque([])
que.append(x)
visited[x]=0


while que:
    now=que.popleft()
    for i in graph[now]:
        if visited[i]==-1:
            visited[i]=visited[now]+1
            que.append(i)


flag=0
for i in range(1,n+1):
    if visited[i]==k:
        flag=1
        print(i)

if flag==0:
    print(-1)

