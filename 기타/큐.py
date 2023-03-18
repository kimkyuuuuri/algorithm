import sys
from collections import deque
num=int(sys.stdin.readline())
queue = deque()
for _ in range(num):
    input_list=list(sys.stdin.readline().split())
    
    if input_list[0]=='push':
        queue.append(int(input_list[1]))
    elif input_list[0]=='pop':
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif input_list[0]=='size':
        print(len(queue))
    elif input_list[0]=='empty':
        if(len(queue)==0):
            print(1)
        else:
            print(0)
    elif input_list[0]=='front':
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
    elif input_list[0]=='back':
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[-1])
 
        
        
