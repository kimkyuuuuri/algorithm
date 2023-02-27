stack = []
stack.append(5)
stack.append(4)
stack.pop()
print(stack)

from collections import deque
queue = deque()
queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.popleft()
print(queue)

queue.reverse()
print(queue)


def recursive_function(i):
    if i==100:
        return
    print(i)
    recursive_function(i+1)


recursive_function(1)
