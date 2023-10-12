#0 1 2 3 / 북 동 남 서
array=[]


dx=[-1,0,1,0]
dy=[0,1,0,-1]
n, m=map(int, input().split())
r,c,d = map(int, input().split())
# 수정 
array.append(list(map(int, input().split())))
answer=0

def bfs(r,c):
    # que에 방향도 함께 저장? // 현재 위치만 가지고 있으면 될 듯 
    global answer
    que=deque([])
    que.append([r,c])

    # while 조건은 벽을 만나면 종료 . 
    while array
        now=que.pop()
        if array[now[0]][now[1]]==0:
            array[now[0]][now[1]]=1
            answer+=1
            que.append([now[0],now[1]])
            continue

        else:
            # 반시계 방향
            flag=0
            for i in range(3,-1,-1):
                d=(d+i)%4
                nx=now[0]+dx[d]
                ny=now[1]+dy[d]
                if nx>=0 and nx<n and ny>=0 and ny<m and array[nx][ny]==0:
                    # 방향 수정하기
                    array[nx][ny]=1
                    answer+=1
                    que.append([nx,ny])
                    flag=1
                    
            if flag==0:
                # 후진. 만약 동쪽으로 .?  뭐 아무튼 방향에 따라서 이동 다르게 할 수 있도록 ! 
            
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    return
                else:
                    
                    nx=
                    array[nx][ny]=1
                    que.append([nx,ny])
                    continue

                # 현재 방향에 따라서 후진! 
                    

                # 방향 바꾸기 
                
         
        nx=now[0]+dx[d]
        ny=now[1]+dy[d]

        if array


# 정리할 것: 후진 어떻게 구현?
# 방향 % (음수일 떄도 ) 이렇게 하면 될까? 나누기 이용 혹은 초기화 ! 
# If 문의 순서 ! -> flag를 사용하는 로직이 맞음 ! 
# 꼭 bfs로 구현하지 않아도 된다 ! 그냥 while문으로 돌아도 된다 ! 
        
    

