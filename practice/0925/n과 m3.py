n,k = map(int, input().split())

def dfs(array):
    if len(array)==k:
        
        print(' '.join(map(str,array)))
        return

    for i in range(0,n):
        
        array.append(i+1)
        dfs(array)
        array.pop()

array=[]
dfs(array)


