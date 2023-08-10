def solution(k, m, score):
    answer = 0
    length=len(score)
    score.sort()
    index = length-m
    
    while index>=0:
        answer+=score[index]*m
        index-=m
        
    return answer
