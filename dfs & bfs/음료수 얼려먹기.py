
def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    
    
    if graph[x][y]==0:
        graph[x][y]=1
        
        print(graph)
        
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
            print("아이스크림 하나 생성 !!")
            print('\n')
            result+=1

print(result)

