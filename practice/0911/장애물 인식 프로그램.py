import sys
from collections import deque
input=sys.stdin.readline

array=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n=int(input())
for i in range(n):
    array.append(list(map(int,input().rstrip())))

def bfs(x,y):
    count=1
    que=deque()
    que.append((x,y))
    array[x][y]=0
    while que:
        now = que.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n :
                continue
            if array[nx][ny]==0:
                continue
            if array[nx][ny]==1:
                que.append((nx,ny))
                array[nx][ny]=0
                count+=1
    return count

answer=0
count=0
answer_array=[]
for i in range(n):
    for j in range(n):
        if array[i][j]==1:
            answer=bfs(i,j)
            answer_array.append(answer)
            count+=1
         

print(count)
answer_array.sort()
for i in answer_array:
    print(i)


