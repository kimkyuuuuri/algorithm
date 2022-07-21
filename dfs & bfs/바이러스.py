n=int(input())
e=int(input())
visited=[False]*(n+1)
graph=[]
graph.append([])
for i in range(e):
    graph.append(list(map(int, input().split())))
for i in range(n-e):
    graph.append([])



visited2=[False]*(n+1)
from collections import deque
def bfs(graph,start,visited2):
    result=0
    queue=deque([start])
    visited2[start]=True
    count=0
    while queue:
        v=queue.popleft()
        print(v)
      
        if graph[v] == []:
           continue;
        
        result+=1
        
        for i in graph[v]:
        
            if not visited2[i]:
                
                if not visited2[graph[v][0]] and not visited2[graph[v][1]] and result!=1:
                    
                    return result-1
                queue.append(i)
                visited2[i]=True
                count+=1
    return result-1

result=bfs(graph,1,visited2)
#print(result)
