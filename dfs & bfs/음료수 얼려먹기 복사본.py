
def dfs(x,y,count):
    if x<0 or y<0 or x>=n or y>=m:
        return 0
    
    
    if graph[x][y]==0:
        graph[x][y]=1
        count+=1
        result_list[x][y]=count
        print(result_list)
        print(count)
        
        dfs(x-1,y,count)
        dfs(x,y-1,count)
        dfs(x+1,y,count)
        dfs(x,y+1,count)
        
        return count
    


n,m=map(int, input().split())
graph=[]
result=0
result_list = [[0 for j in range(m+1)] for i in range(n+1)]
for i in range(n):
    graph.append(list(map(int, input())))
 
for i in range(n):
    for j in range(m):
        n=dfs(i,j,0)
        if n!=0:
            print("아이스크림 하나 생성 !!")
            print('\n')
            result+=1
            print(result_list)

print(result)

