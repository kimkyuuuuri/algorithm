import sys
import heapq

input = sys.stdin.readline
n=int(input())
array =list(map(int, input().split()))
answer_array = [-1]*(n)
stack=[(0,array[0])]

for i in range(1, len(array)):
    while stack[-1][1]<array[i]:
        answer_array[stack[-1][0]]=array[i]
        stack.pop()
    
    stack.append((i, array[i]))

for i in answer_array:
    print(i,end=' ')
    
        
        
