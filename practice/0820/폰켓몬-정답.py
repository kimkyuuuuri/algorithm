import itertools
def solution(nums):
    answer=0
    array=set(nums)
    length=len(array)
    if len(nums)//2<=length:
        answer= len(nums)//2
    else: 
        answer= length
   
    return answer
