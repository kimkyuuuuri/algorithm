import sys
import copy
from collections import deque
input=sys.stdin.readline
n=int(input())
global array
array=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    array.append(list(map(int, input().split())))
    
global now_size
now_size=2
global eat
eat=0


def bfs(x,y):
    que=deque([])
    que.append([x,y])
    answer_list=[]
    visited=[[False]*(n+1) for i in range(n+1)]
    visited[x][y]=0
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny]!=False:
                continue

            # 방문 안한것 중 ! array 값이 더 크다면? 
            if array[nx][ny]>now_size:
                continue
            
            elif array[nx][ny]==now_size or array[nx][ny]==0:
                que.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1

            elif array[nx][ny]<now_size:
                que.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1
                answer_list.append([visited[nx][ny],nx,ny])
              
    if answer_list:
        return sorted(answer_list, key=lambda x:(x[0], x[1], x[2]))
    else:
        return []
                    


answer=0
for i in range(n):
    for j in range(n):
        if array[i][j]==9:
            array[i][j]=0
            while True:
                answer_list=bfs(i,j)
                if len(answer_list)==0:
                    break
                temp=answer_list[0]
                i,j = temp[1],temp[2]
                array[i][j]=0
                eat+=1

                answer+=temp[0]
                if eat==now_size:
                    now_size+=1
                    eat=0
            break
        
print(answer)
            
            



       

                
                
                
        
        
    
