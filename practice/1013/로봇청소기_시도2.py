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

# 가장 먼저 첫 방문. 
answer=1
array[r][c]=-1

def solution(r,c,d):
    answer=1
    x,y=r,c
    
    # 벽을 만나면 종료 
    while array[x][y]!=1:
        flag=0
        # 4번 돌면서 확인 
        for _ in range(4):
            d-=1
            if d<0:
                d=3
            nx=x+dx[d]
            ny=y+dy[d]
            
            # 방문할 곳이 있다면 여기서 바로 방문 ! 첫번째 로직을 여기서 바로 시작 
            if array[nx][ny]==0:
                flag=1
                x=nx
                y=ny
                array[nx][ny]=-1
                answer+=1
                break
            
        # 방문할 곳이 없다면, 후진 
        if flag==0:
            temp=d
            for i in range(2):
                temp-=1
                if temp<0:
                    temp=3
            x=x+dx[temp]
            y=y+dy[temp]
            
    print(answer)
            
            
        
       
        

solution(r,c,d)
#print(answer)
            
            
            
            
            
