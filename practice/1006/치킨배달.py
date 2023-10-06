import sys
input=sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())
array=[]
house_array=[]
chicken_array=[]

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if array[i][j]==1:
            house_array.append([i,j])
        elif array[i][j]==2:
            chicken_array.append([i,j])

candidates=list(combinations(chicken_array,m))
answer_candidate=[]
for i in candidates:
    answer_temp=0
    for j in house_array:
        min_temp=1e9
        for k in i:
            min_temp=min(min_temp, abs(j[0]-k[0])+abs(j[1]-k[1]))
        answer_temp+=min_temp
    answer_candidate.append(answer_temp)
print(min(answer_candidate))
        
            
            
    
