import sys
from bisect import bisect_left, bisect_right
n,q= map(int,input().split())

array = list(map(int, input().split()))
array.sort()
array_len=len(array)
for i in range(q):
    temp=int(input())
    left_index=bisect_left(array,temp )
    right_index=bisect_right(array,temp)
    print(left_index* (array_len-right_index))
   

    
