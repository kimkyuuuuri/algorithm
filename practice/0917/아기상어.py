import sys
from collections import deque
n=int(input())
graph= []
array=[[0]*(n) for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    array.append(list(map(int, input().split())))
    


# dfs 구현
def dfs(array, x,y):
    count=0
    que=deque()
    que.append([x,y])
    
    while que:
        nx, ny = que.popleft()
        for i in range(4):
            nnx=nx+dx[i]
            nny=ny+dy[i]
            if nnx<0 or nny<0 or nnx>=n or nny>=n:
                continue

            que.append([nnx,nny])
            
            
        
        
        
