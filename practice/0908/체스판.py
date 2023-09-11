n,m = map(int, input().split())
graph=[]
graph_2=[[0]*m for i in range(n)]

for i in range(n):
    temp_array=list(input())
    graph.append(temp_array)
    
for i in range(n):
    for j in range(m):
        graph_2[i][j]=graph[i][j]
        
# 처음 바꾸는 경우
# 처음 바꾸지 않는 경우

answer1=0
answer2=0
temp='B'
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            if  temp != graph[i][j]:
                answer1+=1
                graph[i][j]=temp
            continue
        if j==0:
            if temp != graph[i][j] and temp =='B':
                answer1+=1
                graph[i][j]='B'
            elif temp != graph[i][j] and temp =='W':
                answer1+=1
                graph[i][j]='W'
            temp = graph[i][j]
            continue
            
        if temp == graph[i][j] and temp =='B':
            answer1+=1
            graph[i][j]='W'
        elif temp == graph[i][j] and temp =='W':
            answer1+=1
            graph[i][j]='B'
        temp = graph[i][j]

temp='W'

for i in range(n):
    for j in range(m):
    
        
        if i==0 and j==0:
            print(temp)
            print(graph_2[i][j])
            if  temp != graph_2[i][j]:
                answer2+=1
                graph_2[i][j]=temp
            continue
        if j==0:
            if temp != graph_2[i][j] and temp =='B':
                answer2+=1
                graph_2[i][j]='B'
            elif temp != graph_2[i][j] and temp =='W':
                answer2+=1
                graph_2[i][j]='W'
            temp = graph_2[i][j]
            continue
            
        if temp == graph_2[i][j] and temp =='B':
            answer2+=1
            graph_2[i][j]='W'
        elif temp == graph_2[i][j] and temp =='W':
            answer2+=1
            graph_2[i][j]='B'
        temp = graph_2[i][j]
        
print(answer1)
print(answer2)
print(min(answer1,answer2))
        
        
        
    
