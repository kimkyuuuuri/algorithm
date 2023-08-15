from collections import deque

n,m = map(int, input().split())
graph=[[0]*n for i in range(m)]
#예외처리 

first_sum=0
flag=0
for i in range(m):
    temp=list(map(int, input().split()))
    for j in range(n):
        graph[i][j]=temp[j]
        if 0 in temp:
            flag=1
if flag==0:
    print(0)
    print("here!!!")

print(graph)

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(init_x,init_y):
    answer=0
    que=deque()
    que.append((init_x,init_y))

    while que:
        x,y = que.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=m or ny>=n or nx<0 or ny<0:
                continue

            if graph[nx][ny]==1:
                continue
            elif graph[nx][ny]==-1:
                continue
            elif graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y]+1
                que.append((nx,ny))
            else:
                print("here!!!")
                print(graph[nx][ny])
                print(graph[x][y]+1)
                print("비교 " )
             #   graph[nx][ny] = min(graph[nx][ny],graph[x][y]+1)
              #  que.append((nx,ny))
                
                
            
     
for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j)


answer=0
for i in graph:
    if 0 in i:
        print(-1)
       
    answer=max(answer,max(i))
print(graph)
print(answer-1)

                
                
            
            

        


        
