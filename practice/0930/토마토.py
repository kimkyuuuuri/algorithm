import sys
from collections import deque
input= sys.stdin.readline

n,m = map(int, input().split())
array=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
global que
que=deque()

for i in range(m):
    array.append(list(map(int, input().split())))

def bfs(x,y):
    global que
    que.append([x,y])
    answer=0

    while que:
        now=que.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx>=0 and ny>=0 and nx<m and ny<n :
                if array[nx][ny]==-1:
                    continue
                elif array[nx][ny]==0 :
                    array[nx][ny]=array[now[0]][now[1]]+1
                    que.append([nx,ny])
        answer+=1
    return answer


for i in range(m):
    for j in range(n):
        if array[i][j]==1:
            que.append([i,j])
if que:           
    answer=bfs(que[0][0], que[0][1])

result=-1
for i in array:
    result=max(result, max(i))

for i in array:
    if 0 in i:
        result=0
        
print(result-1)

    

    
    

        
    
