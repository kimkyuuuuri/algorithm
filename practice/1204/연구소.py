import copy
from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline

n,m = map(int, input().split())
array=[]
zero=[]

def bfs(array):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    que=deque([])
    for i in range(n):
        for j in range(m):
            if array[i][j]==2:
                que.append([i,j])

    while que:
        now=que.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m :
                continue
            if array[nx][ny]==0:
                array[nx][ny]=2
                que.append([nx,ny])
    result=0
    for i in range(n):
        result+=array[i].count(0)
    return result


  
for i in range(n):
    temp_array=list(map(int, input().split()))
    array.append(temp_array)

for i in range(n):
    for j in range(m):
        if array[i][j]==0:
            zero.append([i,j])


candidate = list(combinations(zero, 3))
temp_answer=0

for i in candidate:
    array2=copy.deepcopy(array)
    for k in i:
        array2[k[0]][k[1]]=1
    temp_answer=max(bfs(array2),temp_answer)
    
    
print(temp_answer)


        
                
    

            


            
