 

from collections import deque

queue=deque()
queue.append(5)
queue.append(2)
queue.append(1)
queue.append(4)
queue.popleft()
print(queue)
queue.reverse()

print(queue)

n=int(input())
queue=deque()
for i in range(n):
    a=input()
    if a.split()[0]=='push':
        queue.append(a.split()[1])
        
    elif a=='top':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    elif a=='size':
        print(len(queue))
    elif a=='pop':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
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
