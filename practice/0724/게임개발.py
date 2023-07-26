n,m = map(int, input().split())
x,y,s = map(int, input().split())
# 0,0 index caution
array=[]
result=0
# 북 동 남 서 
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for i in range(n):
    array.append(list(map(int, input().split())))

index=s-1
for i in range(100):
    # 왼쪽방향 이동
    nx = x+dx[index]
    ny = y+dy[index]
    new_val=array[nx][ny]
    
    # 가보지 않은 칸이 없다면 이동하지 않는다. 인덱스만 수정 
    if new_val==1 or nx<0 or nx>n or ny<0 or ny>m:
        index-=1
        
    # 가보았다면 
    if new_val==1 or nx<0 or nx>n or ny<0 or ny>m:
        index-=1
        
        
    
    
    if index<-4:
        nx=x
        ny=y-1
        index+=4
    if x>n or y>m:
        break
    
    else:
        #left move
        nx = x+dx[index]
        ny = y+dy[index]
        print(index)
    new_val=array[nx][ny]
        
    if new_val==1 or nx<0 or nx>n or ny<0 or ny>m:
        nx=x
        ny=y
        index-=1
        continue
    else:
        result+=1
    
    
        

print(result)
    
    
        
        
        


    

