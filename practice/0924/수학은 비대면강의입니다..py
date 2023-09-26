a,b,c,d,e,f = map(int, input().split())
# 수학 계산으로 풀기? 

for x in range(-999,1000):
    for y in range(-999,1000):
        if (a*x + b*y == c) and d*x + e*y ==f:
            print(x, end=' ')
            print(y)
            break
        
    
