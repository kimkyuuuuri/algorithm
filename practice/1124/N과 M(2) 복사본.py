import sys
input= sys.stdin.readline
n,m = map(int, input().split())

def dfs(i, array):
    if len(array)==m:
        array.sort()
        print(' '.join(map(str, array)))
        return

    for i in range(i,n):
        if i+1 not in array:
            array.append(i+1)
            dfs(i,array)
            array.pop()

array=[]
dfs(0,array)
        
