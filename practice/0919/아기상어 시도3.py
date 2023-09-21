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
    global fish_count
    temp_answer=0
    que=deque()
    que.append([x,y])
    back_x=x
    back_y=y
    #answer_list=[[0,7,7]]
    answer_list=[]
 
    array[x][y]=1

    
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n :
                continue
            # 1
            if array[nx][ny]==0:
                print(big)
                
                print(graph[nx][ny])
                print("---")
                if big>graph[nx][ny] and graph[nx][ny]!=0:
                    #temp_answer=abs(nx-back_x)+abs(ny-back_y)
                    array[nx][ny]=array[x][y]+1
                    fish_count+=1
                    #answer+=temp_answer
                    graph[nx][ny]=0
                    print(nx)
                    answer_list.append([array[nx][ny]-1,nx,ny])
                   
                elif big == graph[nx][ny]:
                    array[nx][ny]=array[x][y]+1
                    que.append([x,y])
                    
                elif graph[nx][ny]==0:
                    array[nx][ny]=array[x][y]+1
                    que.append([x,y])
                  
   
    answer_list.sort(key = lambda x: (x[0], x[1], x[2]))
           
            
    return answer_list
        #print(temp_answer)
  

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
answer_que=deque()
while True:
    
    x_yarray=bfs(graph,init_x,init_y,init_big)
    print(x_yarray)
    if not x_yarray:
        break
    init_x=x_yarray[0][1]
    init_y=x_yarray[0][2]
    
  
    answer+=x_yarray[0][0]
    if fish_count==init_big:
        init_big+=1
        fish_count=0
  
print(answer)
    
    
    
                
            
            
            
        
        
        
