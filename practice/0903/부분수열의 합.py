import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m=map(int, input().split())
array=list(map(int, input().split()))
cnt=0
index=0

def dfs(index,sum_value):
    if index>=n:
        return sum_value
    global cnt
    sum_value+=array[index]
    if sum_value == m:
        cnt+=1
    
    
    
    dfs(index+1, sum_value)
    dfs(index+1, sum_value-array[index])

    

answer=dfs(0,0)
print(cnt)
    
        
    
    
