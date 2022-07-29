n=int(input())

array=list(map(int,input().split()))

import sys
from bisect import bisect_left

lis = []
ans = 0

for num in array:
    if not lis:
       
        lis.append(num)
        ans += 1
        continue
    
    if lis[-1] < num:
        lis.append(num)
        ans += 1
    else:
        index = bisect_left(lis, num)
        lis[index] = num
    
    
print(ans)
