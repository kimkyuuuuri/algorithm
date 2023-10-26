import sys
from collections import deque
input=sys.stdin.readline
n,m = map(int, input().split())
array=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
r,c,d=map(int, input().split())

for i in range(n):
    array.append(list(map(int, input().split())))
answer=0

def bfs(r,c,d,array):
    answer=0
    x,y=r,c
    que=deque([])
    que.append([x,y])
    
    
    while que:
        now=que.popleft()
        if array[now[0]][now[1]]==0:
            array[now[0]][now[1]]=1
            answer+=1
        flag=0
        for _ in range(4):
            d-=1
            if d<0:
                d=3
            nx=x+dx[d]
            ny=y+dy[d]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if array[nx][ny]==0:
                que.append([nx,ny])
                flag=1
                break

        if flag==0:
            temp=d
            for i in range(2):
                temp-=1
                if temp<0:
                    temp=3
          
            nx=x+dx[temp]
            ny=y+dy[temp]
            if nx<0 or ny<0 or nx>=n or ny>=m or array[nx][ny]==1:
                print(array)
                return answer
            que.append([nx,ny])
    return answer

answer=bfs(r,c,d,array)
print(answer)
            
            
            
            
            
