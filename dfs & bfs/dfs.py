def dfs(graph, v, visited):
	visited[v]=True
    print(v,end='')
    #인접한 노드 중 방문하지 않은 것이 있다면 
    for i in graph[v]:
    	if not visited[i]:
        	# 그 i를 기준으로 다시 탐색 시작
        	dfs(graph, i, visitied)


#그래프 표현
graph=[
[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]

#방문된 정보 표현
visited = [False] * 9
dfs(graph, 1, visited)

def dfs(graph, v, visited):
	visited[v]=True
    print(v,end='')
    #인접한 노드 중 방문하지 않은 것이 있다면 
    for i in graph[v]:
    	if not visited[i]:
        	# 그 i를 기준으로 다시 탐색 시작
        	dfs(graph, i, visitied)
