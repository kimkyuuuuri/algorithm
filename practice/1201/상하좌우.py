n=int(input())
array=list(input().split())
x,y = 1,1
# L R U D
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in array:
    direct=0
  
    if i == 'L':
        direct=0
    elif i=='R':
        direct=1
    elif i=='U':
        direct=2
    else:
        direct=3

    nx=x+dx[direct]
    ny=y+dy[direct]

    if nx>n or ny>n or nx<=0 or ny<=0:
        continue
    else:
        x=nx
        y=ny
   

print(y,x)
        
        
    
