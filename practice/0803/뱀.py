import deque
n=int(input())
k=int(input())
array=[[0]*(n+1) for _ in range(n+1)]
#print(apple_array)
#for i in range(k):
count=0
l=int(input())

que=deque()

# 방향 정보는 ??
# 여기서 생각해야할게 항상 특정 지점되면 멈춘다거나 이동한다거나 하면 어떻게 해야할지 모르겠음.
# 방향이니까 동 남 서 북  
dx=[+1, 0, -1, 0 ]
dy=[0, -1, 0, +1 ]

direction=[[] for _ in range(l)]


#사과는 큐에서 넣고 빼고 한다.
#사과가 없다면 꼬리를 지워야함 ! (그래서 큐 이용 )
    
for _ in range(k):
    array[a][b]=1

for i in range(l):
    a,b = map(input().split())
    direction[i].append(int(a), b)
        

x=1
y=1
index=0

while x<=n and y <=n :
    nx = x+dx[index]
    ny = y+dy[index]

    # 만약 count가 차면 index 방향 변경
    
    if array[x][y]==1:
        
        
        
    count+=1
    
