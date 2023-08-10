from collections import deque
import sys
n, m, k, x = map(int, sys.stdin.readline().split())

array = [[] for _ in range(n+1)]
length = [-1] * (n+1)
length[x]=0

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    array[a].append(b)

que=deque([])
que.append(x)

while que:
    v=que.popleft()
    for i in array[v]:
        if length[i]==-1:
            length[i]=length[v]+1
            que.append(i)


flag=0

for i in range(1,n+1):
    if length[i]==k:
        print(i)
        flag=1
        
if flag==0:
    print(-1)
        
    


