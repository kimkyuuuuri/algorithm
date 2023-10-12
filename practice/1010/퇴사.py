n=int(input())
array=[]
answer_array=[]

for i in range(n):
    a,b = map(int, input().split())
    array.append([a,b])


def dfs(day,tmp):
    global answer
    if day==n:
        if answer<tmp:
            answer=tmp
        return
    
    dfs(day+1, tmp)
    if day+array[day][0]<=n:
        dfs(day+array[day][0], tmp+array[day][1])
        
        
answer=0  
dfs(0,0)
print(answer)
        
    

