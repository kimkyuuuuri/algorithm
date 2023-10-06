from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline
n,m = map(int, input().split())
array=[]


house_array=[]
chicken_array=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    temp=list(map(int, input().split()))
    array.append(temp)
    
for i in range(n):
    for j in range(n):
        if array[i][j]==1:
            house_array.append([i,j])
        elif array[i][j]==2:
            chicken_array.append([i,j])

candidates = list(combinations(chicken_array,m))


def bfs(h_x,h_y,visited,candidates):
    count=0
    que=deque()
    visited[h_x][h_y]=1
  
    que.append([h_x, h_y])
    while que:
        now=que.popleft()
        now_x=now[0]
        now_y=now[1]
        for i in range(4):
            new_x=now_x+dx[i]
            new_y=now_y+dy[i]
         
            
            if [new_x, new_y] in candidates:
                return abs(h_x-new_x)+abs(h_y-new_y)
            elif new_x<0 or new_y<0 or new_x>=n or new_y>=n or visited[new_x][new_y]==1:
                continue
            
            else:
                que.append([new_x,new_y])
                visited[new_x][new_y]=1
        

final_answer=[]
for candidate in candidates:
    min_answer=1e9
    answer=[]
    for i in house_array:
        visited=[[0] *(n+1) for i in range(n+1)]
        temp_answer=bfs(i[0],i[1],visited,candidate)
        answer.append(temp_answer)
        
    temp=sum(answer)
    final_answer.append(temp)

print(min(final_answer))
#print(sum(answer))
    
    
    

