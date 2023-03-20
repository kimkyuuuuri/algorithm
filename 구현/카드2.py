import sys
from collections import deque
queue = deque()
num=int(sys.stdin.readline())
for i in range(num):
    queue.append(i+1)

while len(queue)>1:
   
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue.popleft())

