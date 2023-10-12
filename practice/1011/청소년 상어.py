direct_array=[]
number_array=[]
whole_array=[]

dx=[-1,-1,0,1,1, 1, 0, -1]
dy=[0,-1,-1,-1,0,1, 1,1]

for i in range(4):
    temp_list=list(map(int,input().split()))
    number_array.append([temp_list[j] for j in range(8) if j%2==0 ])
    direct_array.append([temp_list[j] for j in range(8) if j%2==1 ])
print(number_array)
print(direct_array) 



# bfs로 구현

def bfs():
    x,y=0,0
    now_turn=direct_array[0][0]
    que=deque([])
    que.append((x,y))
    fish_number=1
    
    
    # 큐를 써야하나? 현재 위치만 저장하고 있으면 되지 않을까?
    # 일단 사용
    
    
        


    # 물고기 한번
    

    
    # 상어 한번- 여러칸 가능
    while que:
    
    
