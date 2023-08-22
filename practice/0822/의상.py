def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic.keys():
            dic[i[1]].append(i[0])
        else:
            dic[i[1]]=[i[0]]
    for i in dic:
        answer*=len(dic[i])+1
    return answer-1
