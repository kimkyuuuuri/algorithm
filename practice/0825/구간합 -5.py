import sys
input = sys.stdin.readline
n,m = map(int, input().split())

graph=[]
temp=[[0]* (n+1) for i in range(n+1)]
result=0

for i in range(n):
    graph.append(list(map(int, input().split())))

# prefix 연산
for i in range(1, n+1):
    for j in range(1, n+1):
        temp[i][j]=temp[i][j-1]+ temp[i-1][j] - temp[i-1][j-1] + graph[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    result= temp[x2][y2] - temp[x1-1][y2] - temp[x2][y1-1] + temp[x1-1][y1-1]
    print(result)
