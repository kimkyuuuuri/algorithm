import sys
input=sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int, input().split())
graph=[]

for i in range(m):
    graph.append(list(map(int, input().split())))

# 큐에 x,y를 넣고 방문하지 않았다면 하나씩 꺼내면서 주의를 다 탐색 ! 
def bfs():
    while que:
        x,y =que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            elif graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                que.append((nx,ny))
    

    # 큐... 

     
que=deque()
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            que.append((i,j))
bfs()
print(graph)

# 그래프에 0 있으면 return -1
# 아니면 최대값

# 처음 탐색하고 싶은 값 넣기  
    
    
