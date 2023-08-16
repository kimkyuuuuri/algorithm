n=input()
import math
array=[0]*10
result=0
for i in n:
    array[int(i)]+=1

for i in range(10):
    if i!=6 and i!=9:
        result=max(result, array[i])
result=max(result, math.ceil((array[6]+array[9])/2))

print(result)

