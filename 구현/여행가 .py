n= int(input())
plans=input().split()
x,y=1,1

dx=[0,0,-1,1]
dy=[-1,1,0,0]

move_types = ['L','R','U','D']

for plan in plans:
	for i in range(len(move_types)):
    # 새로운 배열을 만들어서 비교하기
    	if plan==move_types[i]:
        	nx = x+dx[i]
            ny = y+dy[i]
        if nx<1 or ny<1 or nx>n or ny>n:
        	continue
            
        x,y=nx,ny

print(x,y)
