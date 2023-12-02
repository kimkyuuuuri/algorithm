n=int(input())
array=list(map(int, input().split()))

# 작은 사람 먼저 모으기 ->  그래야 그룹이 많아지니까 ! 
array.sort()

# 반복문 돌면서 그룹을 모을까?
count=0
temp_group=[]
for i in array:
    temp_group.append(i)
    if len(temp_group)==i:
        temp_group=[]
        count+=1
    
print(count)    
