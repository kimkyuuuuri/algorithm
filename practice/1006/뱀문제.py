n=int(input())
k=int(input())

array=[[0]*(n+1) for _ in range(n+1)]
info=[]

for i in range(k):
    a,b = map(int, input().split())
    # 사과 있는 곳 1로 표시 
    array[a][b]=1

l=int(input())
for i in range(l):
    x,c = input().split()
    info.append([int(x),c])

#동남서북
# dx, dy 혼동 금지 
dx=[0,1,0,-1]
dy=[1,0,-1,0]

#turn은 함수로 ! 
def turn(direction, c):
    if c=='L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def simulate():
    x,y=1,1
    array[x][y]=2
    direction=0
    time=0

    # 이거 잘 모르겠음
    index=0
    q=[[x,y]]

    # 부딪히거나,, 등에 끝나니까 종료조건 알 수 없음 
    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]

        if 1 <=nx and nx<=n and 1<=ny and ny<=n and array[nx][ny]!=2:
            if array[nx][ny]==0:
                array[nx][ny]=2
                q.append([nx,ny])
                px, py= q.pop(0)
                array[px][py]=0

            if array[nx][ny]==1:
                array[nx][ny]=2
                q.append([nx,ny])
        else:
            time+=1
            break
        x,y=nx,ny
        time+=1

        if index<l and time==info[index][0]:
            direction=turn(direction, info[index][1])
            index+=1

    return time
print(simulate())
        
        
    
    
