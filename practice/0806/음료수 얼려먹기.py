n,m=map(int, input().split())
graph=[]
count=0
for i in range(n):
    graph.append(list(map(int, input())))
#print(graph)

def dfs(x,y):
    if x<=-1 or y<=-1 or y>=m or x>=n:
        return False
    
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count+=1
print(count)
        
        
            
