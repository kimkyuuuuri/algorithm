
import math 
n=int(input())
for i in range(n):
    array=list(map(int,input().split()))
    distance=math.sqrt((array[0]-array[3])**2+(array[1]-array[4])**2)

    if (array[2]==array[5] and distance==0):
        print(-1)
#내접 외접
    
    elif abs(array[2]-array[5])==distance or array[2]+array[5]==distance:
        print(1)

    elif abs(array[2]-array[5])<distance<array[2]+array[5]:
        print(2)
    else:
        print(0)



