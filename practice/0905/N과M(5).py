n,m = map(int, input().split())
num=list(map(int, input().split()))
num.sort()
array=[]

def dfs():
    if len(array)==m:
        print(' '.join(map(str,array)))
        return

    for i in range( n):
        if num[i] not in array:
            array.append(num[i])
            dfs()
            array.pop()

dfs()
        
