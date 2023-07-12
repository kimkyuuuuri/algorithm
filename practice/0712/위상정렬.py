from collections import deque

v,e= map(int,input().split())
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]
for _ in range(e):
    # 간선의 수 만큼
    a,b = map(int, input().split())
    graph[a].append(b)
    # 들어오는 아이의 간선의 수 만큼 +1 
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)


    while q:
        now=q.popleft()
        result.append(now)
        # now 원소와 연결이 되어 있다면 
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
        for i in result:
            print(i)


topology_sort()
        
