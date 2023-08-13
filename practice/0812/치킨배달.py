from itertools import combinations

n,m = map(int, input().split())
chicken, house = [], []


for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] ==1:
            house.append((r,c))
        elif data[c]==2:
            chicken.append((r,c))

candidates = list(combinations(chicken, m))

# 다 돌면서 계산 
def get_sum(candidate):
    result=0
    for hx, hy in house:
        temp=1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))

        result+=temp
    return result

result = 1e9

# 조합의 후보지 중 최소 선택 
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
    
            
            
