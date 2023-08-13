from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,3))


from itertools import combinations
result = list(combinations(data,3))
print(result)


