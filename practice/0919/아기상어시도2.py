import sys
input=sys.stdin.readline
from collections import deque
n=int(input())
import math
graph= []


# 가장 위, 가장 왼쪽 
dx = [0,-1,1,0]
dy = [-1,0,0,1]
for i in range(n):
    graph.append(list(map(int, input().split())))
    


# dfs 구현
def bfs(graph, x,y, big):
    array=[[0]*(n) for i in range(n)]
    global answer
    global fish_count
    temp_answer=0
    que=deque()
    que.append([x,y])
    back_x=x
    back_y=y
    answer_list=[]
    flag=0
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            # 1
            if array[nx][ny]==0:
                if big < graph[nx][ny]:
                    continue
                que.append([nx,ny])
                array[nx][ny]=array[x][y]+1
                
                
                if big>graph[nx][ny] and graph[nx][ny]!=0:
                    #temp_answer=abs(nx-back_x)+abs(ny-back_y)
                    
                    fish_count+=1
                    #answer+=temp_answer
                    graph[nx][ny]=0
                    answer_list.append([array[nx][ny],nx,ny])
                    flag=1
                    
    if len(answer_list)!=0:
        answer_list.sort(key=lambda x:x[2])
        answer_list.sort(key=lambda x:x[1])
        answer_list.sort(key=lambda x:x[0])
           
            print(answer_list)
            temp_answer=answer_list[0][0]
            answer+=temp_answer
        return answer_list[0]
        #print(temp_answer)
    
    answer+=temp_answer
    #print(answer_list[0])
    return [0,7,7]

init_x=0
init_y=0
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            init_x=i
            init_y=j

init_big=2
fish_count=0
answer=0
while True:
    
    x_yarray=bfs(graph,init_x,init_y,init_big)
    if init_x==7 and init_y==7:
        break
    init_x=x_yarray[1]
    init_y=x_yarray[2]
    if fish_count==init_big:
        init_big+=1
        fish_count=0
  
print(answer)
    
    
    
                
            
            
            
        
        
        
