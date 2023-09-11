import sys
input = sys.stdin.readline
array = list(map(int, input().split()))
dx=[1,-1,0,0]
dy=[0,0,-1,1]
n=array[0]
array.pop(0)
visited = [[0] * (2*n+1) for _ in range(2*n+1)]



answer=0
def dfs(x,y,per,count):
    global answer
    global visited
    if count==n:
        answer+=per
        return
    now_per=per
    visited[x][y]=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx < (2*n+1) and 0<=ny < (2*n+1):
            if visited[nx][ny]==1:
                continue
            else:
                dfs(nx,ny,now_per*(array[i]/100),count+1)
                visited[nx][ny]=0
    
            
    
dfs(n,n,1,0)
print(answer)
