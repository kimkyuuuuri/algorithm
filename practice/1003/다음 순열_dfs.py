import sys
from itertools import permutations
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n= int(input())
array=[]
for i in range(1,n+1):
    array.append(i)
    
answer_array=list(map(int, input().split()))

flag=0
answer=-1

def dfs():
    

for i in permutations(array,n):
    if flag==1:
        answer=list(i)
        break
    if list(i)==answer_array:
        flag=1
    
if answer==-1:
    print(answer)
else:
    for i in answer:
        print(i, end=' ')
