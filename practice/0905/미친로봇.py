array = list(map(float, input().split()))

dx=[1,-1,0,0]
dy=[0,0,-1,1]

n=array[0]
array.pop(0)
result=[]


# 모든 경우의 수 다 탐색해야함 dfs # 확률만 곱하면 합하면서 자연스럽게 경우의 수도 나온다 
# result = [x,y,sum_value]
# 그래프를 그려 해결한다 ! 

answer=0
def dfs(x,y,value,index):
    
    nx=x+dx[index]
    ny=y+dy[index]
    new_value=value*array[index]/100
    
    print(result)
    global answer
    if len(result)>=n and nx==0 and ny==0:
       
        answer+=new_value
        return
    elif len(result)>=n :
        return
    elif index>=4 :
        if nx==0 and ny==0:
            answer+=new_value
        return

    #다른 케이스들어가도 됨! 
    
   
    result.append(index)
    dfs(nx,ny,new_value,index)
    result.pop()
    result.append(index+1)
    dfs(nx,ny,new_value,index+1)
    result.pop()
    

    
dfs(0,0,1,0)      
print(1-answer)
