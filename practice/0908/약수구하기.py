# main에서 계산하기
import math
count=0
answer=0
n,k = map(int, input().split())
for i in range(1,n+1):
    if n%i==0:
        count+=1
        if count==k:
            answer=i
            break
print(answer)
    
