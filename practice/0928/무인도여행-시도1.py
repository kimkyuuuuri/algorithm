import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    global maps2
    global now_count
    global visited
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
       
        if nx>=0 and ny>=0 and nx<len(maps2) and ny<len(maps2[0]) and maps2[nx][ny]!='X' and visited[nx][ny]==False:
            
            visited[nx][ny]=True
            now_count+=int(maps2[nx][ny])
            dfs(nx, ny)
    return now_count

def solution(maps):
    global maps2
    global now_count
    global visitedㄴ
    now_count=0
    
    maps2=maps
    answer= []
    visited=[[False]* (len(maps2[0])+1) for i in range(len(maps)+1)]
    
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps2[i][j]!='X':
      
                visited[i][j]=True
                now_count=int(maps[i][j])
                temp=dfs(i,j)
                if temp!=0:
                    answer.append(temp)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer
