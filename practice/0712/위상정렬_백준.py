from collections import deque
q=deque()
result=[]
n,m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for i in range(n+1)]

for i in range(1,m+1):
    a,b=map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology():
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

topology()
for i in range(n):
    print(result[i],end=' ')
