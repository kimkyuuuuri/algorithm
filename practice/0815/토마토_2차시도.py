from collections import deque

n,m = map(int, input().split())
graph=[[0]*n for i in range(m)]

que=deque()

# 이렇게 해도 됨. 
#graph=[list(map(int, input().split())) for _ in range(n)]

flag=0
for i in range(m):
    temp=list(map(int, input().split()))
    for j in range(n):
        graph[i][j]=temp[j]
        if temp[j]==1:
            que.append((i,j))
        if 0 in temp:
            flag=1
            
if flag==0:
    print(0)
    exit(0)
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs():
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=m or ny>=n or nx<0 or ny<0:
                continue

            if graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y]+1
                que.append((nx,ny))
            
bfs()
for i in graph:
    if 0 in i:
        print(-1)
        exit(0)
    answer=max(answer,max(i))

print(answer-1)

                
                
            
            

        


        
