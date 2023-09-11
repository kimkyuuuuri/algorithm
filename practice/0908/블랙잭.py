from itertools import combinations
# 갱신하기 
n,m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
temp=m
answer=0
for i in combinations(array,3):
    if m- sum(i) <temp and sum(i)-m<=0:
      
        temp=m-sum(i)
        answer=sum(i)
    
    
print(answer)
