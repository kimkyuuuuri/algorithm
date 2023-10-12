n=int(input())
array_person=list(map(int, input().split()))
b,c = map(int, input().split())
answer=0
import math

for i in array_person:
    if b<c:
        answer+=math.floor(i/c)

    elif b>=c:
        answer+=1
        i-=b
        if i>0:
            answer+=math.ceil(i/c)
print(answer)
            
        
    
