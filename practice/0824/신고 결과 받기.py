from collections import Counter
def solution(id_list, report, k):
    report=set(report)
    dic = {i:0 for i in id_list}
    # 이중 배열
    dic_array = {i:[] for i in id_list}
    
    for i in report:
        dic[i.split()[1]]+=1
        dic_array[i.split()[0]].append(i.split()[1])

    stopped_array = [i for i in dic if dic[i] >= k]
    answer=[]
    # 신고한 목록을 report로 넣어야함
    for i in dic_array:
        count=0
        for j in dic_array[i]:
            if j in stopped_array:
                count+=1
        answer.append(count)
  
 
    return answer
