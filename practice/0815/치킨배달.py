from itertools import combinations

n,m = map(int, input().split())
array=[]
house=[]
chicken=[]


for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if array[i][j]==1:
            house.append((i,j))
        elif array[i][j]==2:
            chicken.append((i,j))

#   총 합을 return 

def get_sum (candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+ abs(hy-cy))
        result += temp
    return result
    

candidates = list(combinations(chicken, m))
result=1e9
for candidate in candidates:
    result=min(result,get_sum(candidate))

print(result)
    
    
            
            
        
