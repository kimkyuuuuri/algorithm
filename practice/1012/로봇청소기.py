import sys
input = sys.stdin.readline
array=[]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n, m=map(int, input().split())
r,c,d = map(int, input().split())

for _ in range(n):
    array.append(list(map(int, input().split())))

array[r][c]=-1
answer=1

while array[r][c]!=1:
    #네 구역에 청소 가능한 곳이 있는지 없는지 확인 
    flag= False
    for _ in range(4):
        d-=1
        if d==-1:
            d=3
        nr = r+dx[d]
        nc = c+dy[d]
        
        if array[nr][nc]==0:
            r=nr
            c=nc
            array[r][c]=-1
            answer+=1
            flag=True
            break
        
    if not flag:
        r+=dx[d-2]
        c+=dy[d-2]

print(answer)
# 정리할 것: 후진 어떻게 구현? -> r+=dx[d-2] // c+=dy[d-2]
# 방향 % (음수) 이렇게 하면 될까? 나누기 이용 혹은 초기화 ! 
# If 문의 순서 ! -> flag를 사용하는 로직이 맞음 ! 
# 꼭 bfs로 구현하지 않아도 된다 ! 그냥 while문으로 돌아도 된다 ! 
        
    

