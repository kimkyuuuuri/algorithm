from itertools import combinations

n,m = map(int, input().split())
candidate=[]
house=[]
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if array[i][j]==2:
            candidate.append([i,j])
        elif array[i][j]==1:
            house.append([i,j])
            
            
answer_list=list(combinations(candidate,m))
result_list=[]


for i in answer_list:
    temp_answer=0
    for j in house:
        min_len=1000
        for k in i:
            min_len=min(min_len, abs(k[0]-j[0])+abs(k[1]-j[1]))
        temp_answer+=min_len
        
    result_list.append(temp_answer)
print(min(result_list))
        

  
