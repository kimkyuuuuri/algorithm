n,m = map(int, input().split())
x,y,s = map(int, input().split())
# 0,0 index caution
array=[]
result=0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    array.append(list(map(int, input().split())))

index=s-1
while True:
    if abs(index-s)==4:
        nx=x
        ny=y-1
    
    else:
        nx = x+dx[index]
        ny = y+dy[index]
        
    new_val=array[nx][ny]
        
    if new_val==1 or nx<0 or nx>8 or ny<0 or ny>8:
        index-=1
        continue
    else:
        resut+=1

print(result)
    
    
        
        
        


    

