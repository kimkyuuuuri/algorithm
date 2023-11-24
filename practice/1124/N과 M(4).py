import sys
input=sys.stdin.readline

n,m = map(int, input().split())
array=[]

def dfs(now):
    if len(array)==m:
        array.sort()
        print(' '.join(map(str,array)))
        return

    for i in range(now,n+1):
        array.append(i)
        dfs(i)
        array.pop()

dfs(1)
        
    
