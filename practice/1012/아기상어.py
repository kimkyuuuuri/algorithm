from collections import deque
n=int(input())
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    answer=0
    size=2
    eat_count=0
    que=deque([])
    que.append([x,y])
    visited=[[0]*(n+1) for i in range(n+1)]

    while que:
        
        now=que.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n or array[nx][ny]>size or visited[nx][ny]!=0:
                continue
            
            elif array[nx][ny]==size :
                que.append([nx,ny])
                answer+=1
                visited[nx][ny]=visited[now[0]][now[1]]+1

            elif array[nx][ny]<size:
                que.append([nx,ny])
                array[nx][ny]=0
                eat_count+=1
                visited[nx][ny]=visited[now[0]][now[1]]+1
                

                flag=0
                for j in array:
                        if 1 in j:
                            flag=1
                if flag==0:
                    return visited[now[0]][now[1]]+1
                
                if size==eat_count:
                    temp=visited[now[0]][now[1]]+1
                    print(visited)
                    visited=[[0]*(n+1) for i in range(n+1)]
                    while que:
                        que.popleft()
                    que.append([nx,ny])
                    visited[nx][ny]=temp
                    size+=1
                    eat_count=0
                    
                answer+=1
                
    return answer

final_answer=0
for i in range(3):
    for j in range(3):
        if array[i][j]==9:
            final_answer=bfs(i,j)
print(final_answer)

            
                
    
