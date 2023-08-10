n = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x=1
y=1

array=list( input().split())

for i in array:
    if i=='L':
        nx=x+dx[0]
        ny=y+dy[0]
    elif i=='R':
        nx=x+dx[1]
        ny=y+dy[1]
    elif i=='U':
        nx=x+dx[2]
        ny=y+dy[2]
    else:
        nx=x+dx[3]
        ny=y+dy[3]
        
    if nx==0 or ny==0 or nx>n or ny>n:
        continue

    else:
        x=nx
        y=ny

print(x,end=' ')
print(y)



