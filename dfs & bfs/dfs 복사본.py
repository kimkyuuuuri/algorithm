n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))



def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False

    
    if graph[x][y]==0:
        graph[x][y]=1
        print('\n')
        print(graph)
        print('\n')
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
        # 마지막까지 빈곳을 다 1로 채우고 아이스크림의 수 + 1
            result+=1

print(result)

