array = list(map(int, input().split()))

dx=[1,-1,0,0]
dy=[0,0,-1,1]

n=array[0]
array.pop(0)
graph = [[0] * (2*N+1) for _ in range(2*N+1)]



# 모든 경우의 수 다 탐색해야함 dfs # 확률만 곱하면 합하면서 자연스럽게 경우의 수도 나온다 
# result = [x,y,sum_value]
# 그래프를 그려 해결한다 ! 

answer=0
def dfs(x,y , index,count):
    global answer
    global visited
    if index >= 4:
        return
    if count>n:
        return
    
    nx=x+dx[index]
    ny=y+dy[index]
    #print(index)
    #print(nx)

    #print(ny)

    
    if visited[nx][ny]==-1 or (nx==15 and ny==15):
        visited[nx][ny]=visited[x][y]*array[index]/100
        print(visited[x][y]*array[index]/100)
 
        dfs(nx, ny, index,count+1)
        dfs(nx, ny, index+1,count+1)
    else:
        print(nx)
        print(ny)
        answer+=visited[x][y]*array[index]/100
        return
   

    #다른 케이스들어가도 됨! 
    
    #dfs(nx,ny,new_value,index)
    #dfs(nx,ny,new_value,index+1)
    

    
dfs(n,n,1,0)      
print(1-answer)
