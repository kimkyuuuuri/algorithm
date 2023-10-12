from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline

n,m = map(int, input().split())
array=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    array.append(list(map(int, input().split())))

candidates=[]
virus=[]
wall=[]
for i in range(n):
    for j in range(m):
        if array[i][j]==0:
            candidates.append([i,j])
        elif array[i][j]==2:
            virus.append([i,j])
        elif array[i][j]==1:
            wall.append([i,j])
            

def bfs(array_temp,candidate):
    visited=[[False]* (m+1) for j in range(n+1)]
    answer=0
    que=deque()
    
    for i in candidate:
        visited[i[0]][i[1]]=True

    for i in wall:
        visited[i[0]][i[1]]=True
        
    for i in virus:
        que.append([i[0],i[1]])
        visited[i[0]][i[1]]=True
        
        
    while que:
        now=que.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m or array_temp[nx][ny]==1 or visited[nx][ny]==True:
                continue
            if array_temp[nx][ny]==0:
                que.append([nx,ny])
                visited[nx][ny]=True
    
    for i in range(n):
        for j in range(m):
            if visited[i][j]==False:
                answer+=1
                
    return answer


candidates_list=list(combinations(candidates,3))
answer=0
for candidate in candidates_list:
    answer=max(bfs(array,candidate),answer)
   

print(answer)

