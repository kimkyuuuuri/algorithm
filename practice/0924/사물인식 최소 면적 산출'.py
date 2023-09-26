n,k = map(int, input().split())
dic={}
from itertools import permutations

for i in range(n):
    a,b,c=map(int, input().split())
    if c not in dic.keys():
        dic[c]=[[a,b]]
    else:
        dic[c].append([a,b])

print(dic)


for i in dic.keys():
    for 
    
        
