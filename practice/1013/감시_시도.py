from itertools import permutations, product
n,m = map(int, input().split())
array=[]

for i in range(n):
    array.append(list(map(int, input().split())))

num_array=[[] for i in range(7)]

# 일단 .. 반복문 여러개 써서 그냥 구현하기
count=0
for i in range(n):
    for j in range(m):
        if array[i][j]!=0 and array[i][j]!=6:
            num_array[array[i][j]].append([i,j])
            count+=1
            
print(num_array)
print(count)
candidates=list(product([0,1,2,3],repeat=count))
print(candidates)

def solution(candidate):
    # 각각 몇개인지 ..
    
            
            
# 계산하는 함수
#def dfs():
    
    
