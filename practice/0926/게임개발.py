n,m = map(int, input().split())
x,y,d = map(int, input().split())


array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

def dfs(x,y,count,d,array):
    d_backup=d
   
   
    for i in range(4):
        
        if d==0:
            nx=x
            ny=y-1
            if nx>=0 and ny>=0 and nx<n and ny<n and array[nx][ny]==0 :
                d=3
                break
    
            else:
                d=3
                continue
                
                
        elif d==1:
            nx=x-1
            ny=y
            if nx>=0 and ny>=0 and nx<n and ny<n and array[nx][ny]==0 :
                d=0
                break
            else:
                d=0
                continue
                
        elif d==2:
            nx=x
            ny=y+1
            if array[nx][ny]==0 and nx>=0 and ny>=0 and nx<n and ny<n:
                d=1
                break
            else:
                d=1
                continue

        elif d==3:
            nx=x+1
            ny=y
            
            if nx>=0 and ny>=0 and nx<n and ny<n and array[nx][ny]==0 :
                d=2
                break
            else:
                d=2
                continue

    
    if d_backup==d:
        nx=x+1
        ny=y
  
    if nx>=0 and ny>=0 and nx<n and ny<n and array[nx][ny]==0 :
        array[nx][ny]=1
        dfs(nx,ny,count+1,d,array)
    else:
        count+=1
        print(count)
        return 

array[x][y]=1
dfs(x,y,0,d,array)
        
        
                
        
    
