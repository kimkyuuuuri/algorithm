def solution(targets):
    answer = 1
    array=[]
    targets.sort()
    start=targets[0][0]
    end=targets[0][1]
    for i in targets:
        
        if end>i[0]:
            end=min(end,i[1])
            continue
        else:
            answer+=1
            start=i[0]
            end=i[1]
           
    return answer
