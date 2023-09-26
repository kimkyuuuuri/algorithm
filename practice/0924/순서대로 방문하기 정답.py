import sys
input=sys.stdin.readline
n,m=map(int, input().split())
array=[]


for i in range(n):
    array.append(list(map(int, input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[False]*(n) for i in range(n)]
# dfs 구현
# 방문했으면 1로 만들기
# 몇번을 통해 가는지는 상관 X
# 몇가지가 있는지가 중요

count=0
def dfs(i,j,array,x,y,visited):
    global count
    if i==x and j==y:
        print(visited)
        print("\n")
        count+=1
        return
    
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]

        if nx>=0 and ny>=0 and nx<n and ny<n and visited[nx][ny]==False and array[x][y]==0:
            visited[nx][ny]=True
            dfs(nx,ny,array,x,y,visited)
            visited[nx][ny]=False
            #print(visited)
            #visited[nx][ny]=False



      
startx,starty=map(int, input().split())
startx-=1
starty-=1

for i in range(m-1):
    x,y=map(int, input().split())
    x-=1
    y-=1
    visited[startx][starty]=True
    dfs(startx,starty,array,x,y,visited)
    print(count)
    break
    
    
    startx=x
    starty=y
    
    count=0
    
