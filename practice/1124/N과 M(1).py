import sys
input = sys.stdin.readline

n,m=map(int, input().split())
array=[]

def dfs():
    if len(array)==m:
        print(' '.join(map(str,array)))

    for i in range(n):
        if i+1 not in array:
            array.append(i+1)
            dfs()
            array.pop()

dfs()
