from itertools import combinations
from collections import Counter

weight=[100,200,300,200,500]
weights=Counter(weight)
print(weights)
print(weights.keys())
print(weights.values())


weight_combinations = combinations(weights.keys(),2)
print(list(weight_combinations))
