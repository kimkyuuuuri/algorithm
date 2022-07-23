 

from collections import deque


n=int(input())
queue=deque()
for i in range(n):
    a=input()
    if a.split()[0]=='push':
        queue.append(a.split()[1])
        
    elif a=='size':
        print(len(queue))
        
    elif a=='pop':
        if not queue:
            print(-1)
        else:
            queue.popleft()
           
    elif a=='empty':
        if not queue:
            print(1)
        else:
            print(0)
            
    elif a=='front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            
    elif a=='back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
