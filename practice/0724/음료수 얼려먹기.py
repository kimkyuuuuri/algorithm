n,m = map(int, input().split())
array=[]
result=0

for i in range(n):
    array.append(list(map(int, input())))


# 재귀로 구현 => 함수 정의하기
def dfs(x,y):
    
    if x<0 or y<0 or x>=n or y>=m:
        return False
 
    if array[x][y]==0:
        array[x][y]=1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1
print(result)


        
        
