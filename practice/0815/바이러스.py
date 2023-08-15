from collections import deque
n=int(input())
m=int(input())

graph=[[] for i in range(n+1) ]
visited=[0]*(n+1)
visited[1]=1

for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer=0

def bfs(x):
    que=deque()
    que.append(x)
    
    while que:
        now=que.popleft()
        for i in graph[now]:
            if visited[i]==0:
                visited[i]=1
                que.append(i)
     
bfs(1)
print(sum(visited)-1)

