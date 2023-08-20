from collections import Counter
def solution(participant, completion):
    answer = ''
    count_array=Counter(participant)
    
    for i in completion:
        count_array[i]-=1
    for i in count_array:
        if count_array[i]==1:
            return i
    
    return answer
