#dfs 코드
from collections import deque
n,e,s=map(int,input().split())
visited=[False]*(n+1)
graph=[]
for i in range(e):
    graph.append(list(map(int, input().split())))

#graph.sort()
'''def dfs(graph,v,visited):
    visited[v]=True
    print(v,end='')
    
    for i in graph[v]:
        print("test")
        print(i)
        if not visited[i] :
            dfs(graph,i,visited)

visited = [False] * 9


dfs(graph,1,visited)

visited2=[False]*(n+1)'''
'''def dfs(graph, start_node):
 
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()
 
    ## 시작 노드를 시정하기 
    need_visited.append(start_node)
    
    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
 
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
 
            ## 방문한 목록에 추가하기 
            visited.append(node)
            print(node)
 
            ## 그 노드에 연결된 노드를 
            need_visited.extend(graph[node])
            
    return visited
'''
def dfs(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()
    
    ##시작 노드 설정해주기
    need_visited.append(start_node)
    
    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()
        
 
        ##만약 방문한 리스트에 없다면
        if node not in visited:
 
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            print(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
                
    return visited

dfs(graph,1)

visited2=[False]*(n+1)
def bfs(graph,start,visited2):
    queue=deque([start])
    visited2[start]=True
    while queue:
        v=queue.popleft()
        print(v,end='')
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i]=True

bfs(graph,1,visited2)
