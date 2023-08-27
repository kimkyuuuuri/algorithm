def dfs(sheep, wolf, edges, info ):
    if sheep > wolf:
        answer.append(sheep)
    else:
        return
    
    for p, c in edges:
        if visited[p] and not visited[c]:
            visited[c]=1
            if info[c]==0:
                dfs(sheep+1, wolf, edges, info)
            else:
                dfs(sheep, wolf+1, edges, info)
            visited[c]=0
        
def solution(info, edges):
    global answer
    answer=[]
    global visited
    visited = [0] * len(info)
    visited[0]=1
    dfs(1,0, edges, info)
    
    return max(answer)

