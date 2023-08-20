import itertools
def solution(nums):
    answer = 0
    array=list(map(len,map(set,itertools.combinations(nums,len(nums)//2))))
    answer=max(array)
    return answer
