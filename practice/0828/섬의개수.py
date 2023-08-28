import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(x,y):
    #방문 후 바다로 바꾸기 
    
    if x<0 or x>=y_size or y<0 or y>=x_size:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x+1,y+1)
        dfs(x-1,y+1)
        dfs(x-1,y-1)
        dfs(x+1,y-1)
        return True
    return False

    
while True:
    graph=[]
    answer=0
    x_size,y_size = map(int, input().split())
    if x_size==0 and y_size==0:
        break
    
    for i in range(y_size):
        graph.append(list(map(int, input().split())))

    for i in range(y_size):
        for j in range(x_size):
            if dfs(i,j):
                answer+=1
    print(answer)
                

    
        
        

    
