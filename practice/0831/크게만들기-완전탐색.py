import sys
input= sys.stdin.readline
from itertools import combinations
n,m = map(int, input().split())
number=input()
array=[0]*(10**5)
index=0
for i in combinations(number,n-m):
    result = int(''.join(i))
    index+=1
    array[index]=result

print(max(array))
    
        
