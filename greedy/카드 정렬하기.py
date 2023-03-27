from queue import PriorityQueue
queue = PriorityQueue()
input_num = int(input())


for i in range(input_num):
    queue.put(int(input()))

result=0
count=0
while True:
    if queue.qsize()==1:
        print(result)
        break
    count=queue.get() + queue.get()
    queue.put(count)
    result+=count
  
    
    




    
