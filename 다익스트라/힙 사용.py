import heapq

def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        print(value)
        heapq.heappush(h,value)
        print(h)
    print(h)
    print("test")
    for i in range(len(h)):
    	result.append(heapq.heappop(h))
    return result
    
result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
