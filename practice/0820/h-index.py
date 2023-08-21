from bisect import bisect_right,bisect_left
def solution(citations):
    citations.sort()
    answer=0
    for i in range(len(citations),-1,-1):
        index = bisect_left(citations,i)    
        result=len(citations)-index
        if i==result:
            answer=result
            break
    return answer
