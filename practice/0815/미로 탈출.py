from collections import deque

# 행 열, 규칙 세우기
# 행 열이지만 헷갈리니까 그냥 xy로, 하지만 index 확인할 때는 범위 잘 확인해보기 
n,m = map(int, input().split())
graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x,y):
    que=deque()
    que.append((x,y))

    while que:
        x,y= que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=n or ny>=m or nx<0 or ny<0:
                continue
            
            # 방문하지 않았다면 방문하고 큐에 넣기
            if graph[nx][ny]==0:
                continue
            
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                que.append((nx,ny))
                
    # 마지막 출력인데 index 잘 생각해야됨 0부터 시작했으니 -1하기 
    return graph[n-1][m-1]

print(bfs(0,0))

