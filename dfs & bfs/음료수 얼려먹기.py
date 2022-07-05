
def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    #0을 만났을 때만 True 반환
    
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)

