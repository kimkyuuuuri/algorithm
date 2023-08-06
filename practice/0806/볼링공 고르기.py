from collections import Counter
n,m = map(int, input().split())
result=n*(n-1)/2

array=list(map(int,input().split()))
counter_array=Counter(array)


for i in counter_array.values():
    if i>1:
        result-=i*(i-1)//2
       
print(int(result))
