from collections import deque
n,m = map(int, input().split())
array=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    array.append(list(map(int, input())))

def bfs():
    x,y=0,0
    que=deque()
    que.append([x,y])
   
    while que:
        now=que.popleft()
        for i in range(4):
            
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            
            if nx>=0 and ny>=0 and nx<n and ny<m and array[nx][ny]!=0 :
                if array[nx][ny]==1:
                    array[nx][ny]=array[now[0]][now[1]]+1
                    que.append([nx, ny])
bfs()
print(array[n-1][m-1])
    
            
                
    
