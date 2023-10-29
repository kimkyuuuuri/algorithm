import sys
input=sys.stdin.readline
from collections import deque
n,m,k,x = map(int, input().split())
graph = [[] for i in range(n+1)]
visited=[-1]* (n+1)
count=0

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)


def bfs(now):
    que=deque([])
    que.append(now)
    visited[now]=0
    while que:
        now=que.popleft()
        for i in graph[now]:
            if visited[i]==-1:
                visited[i]=visited[now]+1
                que.append(i)
            


bfs(x)
answer_list=[]

for i in range(1, n+1):
    if visited[i]==k:
        answer_list.append(i)

if not answer_list:
    print(-1)
else:
    for i in answer_list:
        print(i)
