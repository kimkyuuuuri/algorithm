n,m = map(int, input().split())
array=[]

def dfs(array):
    if len(array)==m:
        for j in array:
            print(j, end=' ')
        print(end='\n')
        return 

    for i in range(1,n+1):
        array.append(i)
        dfs(array)
        array.pop()

dfs(array) 
