n,m = map(int, input().split())
num = list(map(int, input().split()))
array=[]
num.sort()

def dfs():
    if len(array)==m:
        print(' '.join(map(str, array)))
        return

    for i in range(n):
        array.append(num[i])
        dfs()
        array.pop()

dfs()
