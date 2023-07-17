import sys
from collections import deque
n,m,k,x = map(int, input().split())
graph= [[] for i in range(n+1)]
distance = [-1]*(n+1)
for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)

def bfs(x):
    distance[x]=0
    q=deque([x])
    
    while q:
        now=q.popleft()
        
        for i in graph[now]:
            if distance[i]==-1:
            
                distance[i]=distance[now]+1
                q.append(i)

bfs(x)
answer=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        answer=True


if answer==False:
    print(-1)
  
        
            
        
        
        
    
    
