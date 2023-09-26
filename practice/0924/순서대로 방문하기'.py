import sys
input=sys.stdin.readline
n,m=map(int, input().split())
array=[]


for i in range(n):
    array.append(list(map(int, input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]



count=0
visited=[]
goal=[]
def dfs(i,j,array,visited):
    global count
    if i==goal[-1][0] and j==goal[-1][1]:
        flag=0
        for i in goal:
            if i not in visited:
                 flag=1
        if flag==0:
            count+=1
        return
    
   
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
       
        if nx>=0 and ny>=0 and nx<n and ny<n  and array[nx][ny]==0 :
    
           
            array[nx][ny]=1
            visited.append([nx,ny])
            dfs(nx,ny,array,visited)
            visited.pop()
            array[nx][ny]=0
           

for i in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    goal.append([a,b])



startx,starty=goal[0][0],goal[0][1]
array[startx][starty]=1
visited.append([startx,starty])
dfs(startx,starty,array,visited)
print(count)
