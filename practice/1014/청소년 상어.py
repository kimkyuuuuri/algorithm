import sys
from collections import deque
import copy
input=sys.stdin.readline

array = [[] for i in range(4)]

dx=[0,-1,-1,0,1,1,1,0,-1]
dy=[0,0,-1,-1,-1,0,1,1,1]


for i in range(4):
    temp_array=list(map(int, input().split()))
    for j in range(len(temp_array)//2):
        array[i].append(temp_array[j*2:j*2+2])

          
max_score=0
def dfs(x,y,score,array):
    # 밖에서도 max_score 사용할 수 있음. 
    global max_score
    score+=array[x][y][0]
    # 물고기 먹고
    max_score=max(max_score, score)
    #상어가 있는 곳은 0으로 표시 
    array[x][y][0]=0
    
    # 물고기 이동 
    for i in range(1,17):
        temp_j, temp_k= -1,-1
        for j in range(4):
            for k in range(4):
                if array[j][k][0]==i:
                    temp_j, temp_k=j,k
                    break
                
        if temp_j == -1 and temp_k==-1:
            continue
            
        temp_d=array[temp_j][temp_k][1]
        for td in range(8):
            nd=(temp_d+td)%9
            if nd==0:
                nd=1
                
           
           
            nx=temp_j+dx[nd]
            ny=temp_k+dy[nd]
                        # 상어를 만나면 
            if nx<0 or ny<0 or nx>=4 or ny>=4 or (nx==x and ny==y):
                continue
        
                            # 위치 바꿈
            array[temp_j][temp_k][1]=nd
            array[nx][ny], array[temp_j][temp_k]=array[temp_j][temp_k],array[nx][ny]
            break
    d=array[x][y][1]
    # 그 방향으로 최대 2번인가 보다
   
    for i in range(1,5):
        nx=x+dx[d]*i
        ny=y+dy[d]*i
        if (0<=nx<4 and 0<=ny <4) and array[nx][ny][0]>0:
            dfs(nx, ny, score, copy.deepcopy(array))


dfs(0,0,0,array)
print(max_score)


