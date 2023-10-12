n,m = map(int, input().split())

array=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    array.append(list(map(int, input())))

def dfs(x,y):
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and ny>=0 and ny<m and nx<n:
            if array[nx][ny]==0:
                array[nx][ny]=1
                dfs(nx,ny)


count=0
print(array)
for i in range(n):
    for j in range(m):
        if array[i][j]==0:
            dfs(i,j)
            count+=1
print(count)
            
